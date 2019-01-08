import numpy as np
import cv2
import pytesseract as pyt
import re


kernel_sharpening = np.array([[-1,-1,-1], 
                                [-1, 9,-1],
                                [-1,-1,-1]])


def recognise_text(image_path, template_type, photo_path):
    image = cv2.imread(image_path)

    face, found = get_photo(image)

    if found:
        cv2.imwrite(photo_path, face)
    else:
        photo_path = face

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    luminance, a, b = cv2.split(lab)

    hist,bins = np.histogram(luminance,256,[0,256])

    mean = int((np.argmax(hist) + np.argmin(hist)) / 2)

    luminance[luminance > mean] = 255
    luminance[luminance <= mean] = 0

    cv2.imwrite('luminance.jpg', luminance)

    template = cv2.imread(template_type, 0)
    
    ret3, template = cv2.threshold(template, 220, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    luminance = np.subtract(template, luminance)
    luminance = np.invert(luminance)

    text = pyt.image_to_string(luminance, config=('--oem 1 --psm 3'))
    data = list(text.split('\n'))

    detected_text = clean_text(data)

    return detected_text, photo_path


def recognise_text_wo_template(image_path, photo_path):
    image = cv2.imread(image_path)

    face, found = get_photo(image)

    if found:
        cv2.imwrite(photo_path, face)
    else:
        photo_path = face

    image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.filter2D(image, -1, kernel_sharpening)
    image = cv2.GaussianBlur(image, (3, 3), 0)
    image = cv2.filter2D(image, -1, kernel_sharpening)
    image = cv2.GaussianBlur(image, (3, 3), 0)

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    luminance, a, b = cv2.split(lab)

    hist,bins = np.histogram(luminance,256,[0,256])

    mean = int((np.argmax(hist) + np.argmin(hist)) / 2)

    luminance[luminance > mean] = 255
    luminance[luminance <= mean] = 0

    cv2.imwrite('luminance.jpg', luminance)

    text = pyt.image_to_string(luminance, config=('--oem 1 --psm 3'))
    data = list(text.split('\n'))

    detected_text = clean_text(data)
    
    return detected_text, photo_path


def clean_text(text_list):
    my_list = []
    for i in text_list:
        if i != ' ' or i != '  ' or i != '':
            i = re.sub('[^A-Za-z0-9-/ ]+', '', i)
            shortword = re.compile(r'\W*\b[^0-9/]\w{1,2}\b')
            i = shortword.sub('', i)
            i = i.lstrip()
            i = i.rstrip()
            i = re.sub('\s{2,}', '', i) 
            if i == '':
                continue
            my_list.append(i)
    return my_list


def get_photo(image):
    '''
    Image Should be 1920 x 1080 pixels
    '''
    scale_factor = 1.1
    min_neighbors = 3
    min_size = (150, 150)
    flags = cv2.CASCADE_SCALE_IMAGE

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor, minNeighbors = min_neighbors,
                                          minSize = min_size, flags = flags)
    
    try:
        x, y, w, h = faces[0]
        face = image[y-50:y+h+40, x-10:x+w+10]
        return face, True
    except Exception as e:
        return "Photo not found!", False
