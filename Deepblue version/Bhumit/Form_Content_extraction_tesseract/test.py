import cv2
import numpy as np
import pytesseract as pt


def x_cord_contours(contour):
    if cv2.contourArea(contour) > 10:
        M = cv2.moments(contour)
        return (int(M['m10'] / M['m00']))


def makeSquare(not_square):
    # This function takes an image and makes the dimenions square
    # It adds black pixels as the padding where needed

    BLACK = [0, 0, 0]
    img_dim = not_square.shape
    height = img_dim[0]
    width = img_dim[1]
    #print("Height = ", height, "Width = ", width)
    if (height == width):
        square = not_square
        return square
    else:
        doublesize = cv2.resize(
            not_square, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
        height = height * 2
        width = width * 2
        #print("New Height = ", height, "New Width = ", width)
        if (height > width):
            pad = (height - width) / 2
            pad = int(pad)
            #print("Padding = ", pad)
            doublesize_square = cv2.copyMakeBorder(
                doublesize, 0, 0, pad, pad, cv2.BORDER_CONSTANT, value=BLACK)
        else:
            pad = (width - height) / 2
            pad = int(pad)
            #print("Padding = ", pad)
            doublesize_square = cv2.copyMakeBorder(
                doublesize, pad, pad, 0, 0, cv2.BORDER_CONSTANT, value=BLACK)
    doublesize_square_dim = doublesize_square.shape
    #print("Sq Height = ", doublesize_square_dim[0], "Sq Width = ", doublesize_square_dim[1])
    return doublesize_square


def resize_to_pixel(dimensions, image):
    # This function then re-sizes an image to the specificied dimenions

    buffer_pix = 4
    dimensions = dimensions - buffer_pix
    squared = image
    r = float(dimensions) / squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    width_r = img_dim2[1]
    BLACK = [0, 0, 0]
    if (height_r > width_r):
        resized = cv2.copyMakeBorder(
            resized, 0, 0, 0, 1, cv2.BORDER_CONSTANT, value=BLACK)
    if (height_r < width_r):
        resized = cv2.copyMakeBorder(
            resized, 1, 0, 0, 0, cv2.BORDER_CONSTANT, value=BLACK)
    p = 2
    ReSizedImg = cv2.copyMakeBorder(
        resized, p, p, p, p, cv2.BORDER_CONSTANT, value=BLACK)
    img_dim = ReSizedImg.shape
    height = img_dim[0]
    width = img_dim[1]
    #print("Padded Height = ", height, "Width = ", width)
    return ReSizedImg


# Read blank form
form = cv2.imread('vrkIj.png', cv2.IMREAD_GRAYSCALE)
form = np.array(form)
#form = cv2.GaussianBlur(form, (5,5), 0)
form = cv2.threshold(
    form, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('Form', form)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# fill_form = cv2.imread('simpleformfill.jpg', cv2.IMREAD_GRAYSCALE)
# fill_form = np.array(fill_form)
# #fill_form = cv2.GaussianBlur(fill_form, (5,5), 0)
# fill_form = cv2.threshold(fill_form, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# cv2.imshow('Filled Form', fill_form)
# cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # Subtracting fill_form - form to get the difference fields in images of the form
# result = np.subtract(fill_form, form)
# # Applying Inverse Thresholding to get white background
# result = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# im2, contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# text = []

# for c in contours:
#   (x,y,w,h) = cv2.boundingRect(c)
#   if w>=17 and h>=17:
#       roi = result[y:y+h, x:x+w]
#       squared = makeSquare(roi)
#       txt = pt.image_to_string(squared)

#   text.append(txt)

# print(text[len(text) - 1])
txt = pt.image_to_string(form)
print(txt)
cv2.destroyAllWindows()
