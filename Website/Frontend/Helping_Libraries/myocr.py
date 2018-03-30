import numpy as np
import cv2
import tensorflow as tf
tf.reset_default_graph()
from keras.models import load_model
from keras.preprocessing import image as im
from keras import backend as k
import Helping_Libraries.spell_corrector as sc
import Helping_Libraries.word_segmentor as ws

label_dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
                    11: 'b', 12: 'd', 13: 'e', 14: 'f', 15: 'g', 16: 'h', 17: 'i', 18: 'j', 19: 'l', 20: 'm',
                    21: 'n', 22: 'q', 23: 'r', 24: 't', 25: 'y', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E',
                    31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O',
                    41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y',
                    51: 'Z'}

def testing():
    print('Hello My OCR')

def remove_punctuations(temp_string):
    temp_string = re.sub(r'[^\w]', ' ', temp_string)
    return temp_string


# Preprocess images
def preprocess(image):
    #print(image)
    image = cv2.imread(image,0)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return image

# Preprocessing helper methods
def cropImage(x, y, w, h, image):
    # Crop image here
    #print(x,y,w,h)
    croppedImage = image[y:y + h,x:x + w]
    return croppedImage

def templateMatching(wholeimage, template):
    result = cv2.matchTemplate(wholeimage, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_loc[0], max_loc[1]

def makeSquare(not_square):
    # Adds black pixels as padding

    BLACK = [0, 0, 0]
    img_dim = not_square.shape
    height = img_dim[0]
    width = img_dim[1]
    if (height == width):
        square = not_square
        return square
    else:
        doublesize = cv2.resize(not_square, (2 * width, 2 * height), interpolation = cv2.INTER_CUBIC)
        height = height * 2
        width = width * 2
        if (height > width):
            pad = (height - width)/2
            pad = int(pad)
            #doublesize = int(doublesize)
            doublesize_square = cv2.copyMakeBorder(doublesize, 0, 0, pad,\
                                                  pad, cv2.BORDER_CONSTANT, value = BLACK)
        else:
            pad = (width - height)/2
            pad = int(pad)
            doublesize_square = cv2.copyMakeBorder(doublesize, pad, pad, 0, 0,\
                                                  cv2.BORDER_CONSTANT, value = BLACK)
    doublesize_square_dim = doublesize_square.shape
    return doublesize_square

def resize_to_pixel(dimensions, image):

    buffer_pix = 4
    dimensions = dimensions - buffer_pix
    squared = image
    r = float(dimensions)/squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    widht_r = img_dim2[1]
    BLACK = [0, 0, 0]
    if (height_r > widht_r):
        resized = cv2.copyMakeBorder(resized, 0, 0, 0, 1, cv2.BORDER_CONSTANT, value = BLACK)
    if (height_r < widht_r):
        resized = cv2.copyMakeBorder(resized, 1, 0, 0, 0, cv2.BORDER_CONSTANT, value = BLACK)
    p = 2
    ReSizedImg = cv2.copyMakeBorder(resized, p, p, p, p, cv2.BORDER_CONSTANT, value = BLACK)
    img_dim = ReSizedImg.shape
    height = img_dim[0]
    width = img_dim[1]
    return ReSizedImg


def prediction(char_image, model):

    squared = makeSquare(char_image)
    size28 = resize_to_pixel(28, squared)
    ##cv2.imshow('char resized', size28)
    ##cv2.waitKey(0)
    #cv2.destroyAllWindows()
    predict_img = im.img_to_array(size28)
    predict_img = np.expand_dims(predict_img, axis = 0)
    #print(predict_img.shape)
    predictedarray = model.predict(predict_img)
    index = calculateClass(predictedarray[0])

    predicted_class = label_dictionary[index]
    return predicted_class

def calculateClass(predictedarray):
    predictedclass = 0
    predictedclassindex = 0
    index = 0
    for classprediction in predictedarray:
        if classprediction > predictedclass:
            predictedclass = classprediction
            predictedclassindex = index
        index = index + 1
    return predictedclassindex

def ocrit(image, model):

    # detecting edges in the image
    image_edges = cv2.Canny(image, 30, 150)

    # dilating image to detect individual lines
    kernel_line = np.ones((10, 80), np.uint8)
    dilated_line = cv2.dilate(image_edges, kernel_line, iterations=1)

    # finding contours of the line
    im2, ctrs_line, hier = cv2.findContours(dilated_line.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs_line = sorted(ctrs_line, key=lambda ctr: cv2.boundingRect(ctr)[1])

    # list of words
    word_list = []

    for i, ctr_line in enumerate(sorted_ctrs_line):
        # getting coordinates of the line contour
        line_x, line_y, line_w, line_h = cv2.boundingRect(ctr_line)

        # if condition for removing unnecessary contours
        if line_w * line_h < 10000:
            continue

        line = cropImage(line_x, line_y, line_w, line_h, image)
        #cv2.imshow('line', line)
        #cv2.waitKey(0)

        # detecting edges in the image
        line_edges = cv2.Canny(line, 30, 150)

        # dilating line to detect individual words
        kernel_word = np.ones((10, 60), np.uint8)
        dilated_word = cv2.dilate(line_edges, kernel_word, iterations=1)

        # finding contours of the word
        im2, ctrs_word, hier = cv2.findContours(dilated_word.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sorted_ctrs_word = sorted(ctrs_word, key=lambda ctr: cv2.boundingRect(ctr)[0])

        for i, ctr_word in enumerate(sorted_ctrs_word):
            # getting coordinates of the word contour
            word_x, word_y, word_w, word_h = cv2.boundingRect(ctr_word)

            # if condition for removing unnecessary contours
            if word_w * word_h < 2500:
                continue

            #print("Word " + str(word_x), str(word_y), str(word_w), str(word_h))

            word = cropImage(word_x, word_y, word_w, word_h, line)
            #cv2.imshow('word', word)
            #cv2.waitKey(0)
            word = cv2.erode(word, np.ones((1, 1), np.uint8), iterations=1)

            # detecting edges in the image
            word_edges = cv2.Canny(word, 30, 150)

            # dilating word to detect individual characters
            kernel_char = np.ones((15, 5), np.uint8)
            dilated_char = cv2.dilate(word_edges, kernel_char, iterations=1)
            #cv2.imshow('dilated_char', dilated_char)
            #cv2.waitKey(0)

            # finding contours of the characters
            im2, ctrs_char, hier = cv2.findContours(dilated_char.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            sorted_ctrs_char = sorted(ctrs_char, key=lambda ctr: cv2.boundingRect(ctr)[0])

            # list of words
            character_list = []

            for i, ctr_char in enumerate(sorted_ctrs_char):
                # getting coordinates of the character contour
                char_x, char_y, char_w, char_h = cv2.boundingRect(ctr_char)

                # if condition for removing unnecessary contours
                if char_w * char_h < 180:
                    continue

                #print("Character " + str(char_x), str(char_y), str(char_w), str(char_h))

                charac = cropImage(char_x, char_y, char_w, char_h, word)
                #cv2.imshow('charac', charac)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()
                #print(charac.shape)
                character = prediction(charac, model)

                character_list.append(character)
                #print('OCRit',character)
            word_list.append("".join(character_list))
    recognized_text = " ".join(word_list)
    #print(recognized_text)
    return recognized_text

# cropping and setdifferencing function
def getNonfilledCroppedSections(nonfilledimage, filledimage, nonfilledimagedilated, filledimagedilated, coordinates):
    i = 0
    formvalues = []
    tf.reset_default_graph()
    model = load_model('finalbestmodel.hdf5')
    for key, value in coordinates.items():
        label = key
        value = ast.literal_eval(value)
        x, y, w, h = value
        x, y, w, h = int(x), int(y), int(w), int(h)

        # cropping non filled image
        nonfilledcroppedsection = cropImage(x, y, w, h, nonfilledimage)
        #cv2.imshow('nonfilledcroppedsection', nonfilledcroppedsection)
        #cv2.waitKey(0)

        #dilating
        nonfilledcroppedsectiondilated = cropImage(x, y, w, h, nonfilledimagedilated)

        crop_h = nonfilledcroppedsection.shape[0]
        crop_w = nonfilledcroppedsection.shape[1]

        buffer_x = x - 75
        buffer_y = y - 75
        buffer_w = w + 2*75
        buffer_h = h + 2*75

        if ( buffer_x < 0 ):
            buffer_x = 0
        if ( buffer_y < 0 ):
            buffer_y = 0
        if ( buffer_x + buffer_w > filledimage.shape[0] ):
            buffer_w = filledimage.shape[0]
        if ( buffer_y + buffer_h > filledimage.shape[1] ):
            buffer_h = filledimage.shape[1]

        filledcroppedsectionbuffer = cropImage(buffer_x, buffer_y, buffer_w, buffer_h, filledimagedilated)
        filledcroppedsectionbuffernondilated = cropImage(buffer_x, buffer_y, buffer_w, buffer_h, filledimage)

        crop_x, crop_y = templateMatching(filledcroppedsectionbuffernondilated, nonfilledcroppedsection)

        # cropping the matched template from filled image
        filledcroppedsection = cropImage(buffer_x + crop_x, buffer_y + crop_y, crop_w, crop_h, filledimage)

        # subtracting nonfilled image from filled image
        setDifference = np.subtract(filledcroppedsection, nonfilledcroppedsection)
        #cv2.imshow('setDifference', setDifference)
        #cv2.waitKey(0)

        setDifference = cv2.medianBlur(setDifference, 3)
        #setDifference = cv2.erode(setDifference, np.ones((3, 3), np.uint8), iterations=1)
        #cv2.imshow('setDifferenceeroded', setDifference)
        #cv2.waitKey(0)

        converted_to_text = ocrit(setDifference, model)
        #print('NFcropped Section',converted_to_text)
        formvalues.append([str(i), label, converted_to_text])
        i = i + 1
        #tf.reset_default_graph()
    return formvalues
