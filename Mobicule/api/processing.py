import numpy as np
import cv2
import pytesseract as pyt

def testing(one, two):
	print(one)
	print(two)
	return "Thanks"

def recognise_text(image_path, template_type):
    image = cv2.imread(image_path)
    cv2.imwrite('im.jpg', image)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    luminance, a, b = cv2.split(lab)

    hist,bins = np.histogram(luminance,256,[0,256])

    mean = int((np.argmax(hist) + np.argmin(hist)) / 2)

    luminance[luminance > mean] = 255
    luminance[luminance <= mean] = 0
    cv2.imwrite('im.jpg', luminance)
    template = cv2.imread(template_type, 0)
    cv2.imwrite('temp.jpg', template)
    
    ret3, template = cv2.threshold(template, 220, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    luminance = np.subtract(template, luminance)
    luminance = np.invert(luminance)

    text = pyt.image_to_string(luminance)
    data = text.replace("#", "4").replace("'", "").replace('"', '').replace('!', 'I').replace(']', 'I').upper().split('\n')
    
    return list(data)

def pre_process(template, image):
    template = cv2.imread(template, 0)
    image = cv2.imread(image, 0)
    ret3, template = cv2.threshold(template, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Sharpening the image
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    unsharp_image = cv2.filter2D(image, -1, kernel)

    # Adaptive Thresholding
    # OBinary = cv2.adaptiveThreshold(unsharp_image,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,15,5)

    # Thresholding
    ret3, OBinary = cv2.threshold(unsharp_image, 220, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    #     OBinary = imutils.skeletonize(OBinary, size=(3, 3))
    # OBinary = cv2.medianBlur(OBinary, 5)
    
    # Eroding
    kernel = np.ones((2, 2), np.uint8)
    OBinary = cv2.erode(OBinary, kernel, iterations = 2)
    
    # Subtracting from template
    subtract = np.subtract(OBinary, template)
    cv2.imwrite('sub.jpg', subtract)
    return subtract

def get_text(image):
    
    # getting edges of the text in image
    image_edges = cv2.Canny(image, 30, 150)
    
    # dilating image to detect individual lines
    kernel_line = np.ones((2, 100), np.uint8)
    dilated_line = cv2.dilate(image_edges, kernel_line, iterations=1)
    cv2.imwrite('dilate.jpg', dilated_line)
    # finding contours of the line
    im2, ctrs_line, hier = cv2.findContours(dilated_line.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs_line = sorted(ctrs_line, key=lambda ctr: cv2.boundingRect(ctr)[1])
    
    text = []

    for i, ctr_line in enumerate(sorted_ctrs_line):
        # getting coordinates of the line contour
        x_line, y_line, w_line, h_line = cv2.boundingRect(ctr_line)
        if w_line * h_line < 3000 or w_line * h_line > 50000:
            continue
            
        cropped_line = image[y_line:y_line + h_line, x_line:x_line + w_line]
        # cropped_line = np.invert(cropped_line)
        cv2.imwrite('cropped' + str(i) + '.jpg', cropped_line)
        line_text = pyt.image_to_string(cropped_line)
        line_text = line_text.replace('/', 'i').replace("#", "4").replace("'", "").replace('"', '').replace('!', 'I').replace(']', 'I').upper()
        if line_text != '':
            print(line_text)
            text.append(line_text)
    return text
