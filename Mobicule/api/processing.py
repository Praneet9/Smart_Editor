import cv2
import pytesseract as pyt
import re
from ctpn.demo_pb import get_coords


def recognise_text_wo_template(image_path, photo_path):
    
    image = cv2.imread(image_path, 0)

    coordinates = get_coords(image_path)

    detected_text = []

    coordinates = sorted(coordinates, key = lambda coords: coords[1])

    for coords in coordinates:
        x, y, w, h = coords
        temp = image[y:h, x:w]

        _, thresh = cv2.threshold(temp, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        thresh = cv2.copyMakeBorder(thresh, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        text = pyt.image_to_string(thresh, lang="eng+hin", config=('--oem 1 --psm 3'))
        
        text = clean_text(text)
        if len(text) < 3:
            continue
        detected_text.append(text)

    face, found = get_photo(image)

    if found:
        cv2.imwrite(photo_path, face)
    else:
        photo_path = face
    
    return detected_text, photo_path


def clean_text(text):
    if text != ' ' or text != '  ' or text != '':
        text = re.sub('[^A-Za-z0-9-/ ]+', '', text)
        text = text.lstrip()
        text = text.rstrip()
        text = re.sub(r'\s{2,}', ' ', text) 
        
    return text


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
    except Exception as _:
        return "Photo not found!", False
