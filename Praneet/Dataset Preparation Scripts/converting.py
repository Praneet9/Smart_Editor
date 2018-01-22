import os, PythonMagick
from PythonMagick import Image
from datetime import datetime
import PyPDF2
import numpy as np
import cv2
from imutils import contours
import imutils

start_time = datetime.now()

def x_cord_contour(cnts):
    
    if cv2.contourArea(cnts) > 5:
        M = cv2.moments(cnts)
        return (int(M['m10']/M['m00']))
    
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

a = 0

"""def detection(image):

    img_scaled = cv2.resize(image, None, fx = 0.36, fy = 0.36)
    
    gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)

    # Blur image then find edges using Canny
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edged = cv2.Canny(blurred, 30, 150)

    # Find contours
    ret, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort out contours left to right by using their x coordinates
    #contours = sorted(contours, key = x_cord_contour(contours), reverse = False)


    (cnts, boundingBoxes) = contours.sort_contours(cnts, method="top-to-bottom")
    clone = image.copy()



    # Loop over the contours
    # for (i, c) in enumerate(contours)
    # for c in contours:
    
    for c in cnts:
        # computing bounding box for rectangle
        (x, y, w, h) = cv2.boundingRect(c)
        
        if w >=17 and h >=17:
            roi = blurred[y:y +h, x:x + w]
            ret, roi = cv2.threshold(roi, 200, 255, cv2.THRESH_BINARY_INV)
            # roi = int(roi)
            squared = makeSquare(roi)
            final = resize_to_pixel(28, squared)
            l = str(a)
            #cv2.imshow("final", final)
            cv2.imwrite("./Detected/Demo/img_"+l+".jpg",final)
            a= a + 1
            cv2.waitKey(0)
"""


pdf_dir = r"./Output_PDFs/"
img_dir = r"./Images/"
bg_colour = "#ffffff"

from PyPDF2 import PdfFileWriter, PdfFileReader 
infile = PdfFileReader(open('./New_Folder/page-01.pdf', 'rb'))

for i in range(infile.getNumPages()):
    p = infile.getPage(i)
    outfile = PdfFileWriter()
    outfile.addPage(p)
    with open('./Output_PDFs/page-%02d.pdf' % i, 'wb') as f:
        outfile.write(f)

i = 0

for pdf in [pdf_file for pdf_file in os.listdir(pdf_dir) if pdf_file.endswith(".pdf")]:

    input_pdf = pdf_dir + pdf
    img = Image()
    img.density('300')
    img.read(input_pdf)

    size = "%sx%s" % (img.columns(), img.rows())

    output_img = Image(size, bg_colour)
    output_img.type = img.type
    output_img.composite(img, 0, 0, PythonMagick.CompositeOperator.SrcOverCompositeOp)
    output_img.resize(str(img.rows()))
    output_img.magick('JPG')
    output_img.quality(75)


    #output_jpg = input_pdf.replace(".pdf", ".jpg")
    output_jpg = img_dir + "img_" + str(i) + ".jpg"
    i += 1
    output_img.write(output_jpg)


for img in [img_file for img_file in os.listdir(img_dir) if img_file.endswith(".jpg")]:

    input_img = img_dir + img
    image = cv2.imread(input_img)
    
    img_scaled = cv2.resize(image, None, fx = 0.30, fy = 0.30)
    cv2.imshow('Resized',img_scaled)
    cv2.waitKey()
    
    gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)

    # Blur image then find edges using Canny
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edged = cv2.Canny(blurred, 30, 150)
    cv2.imshow('Edges', edged)
    cv2.waitKey(0)

    # Find contours
    ret, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Sort out contours left to right by using their x coordinates
    #contours = sorted(contours, key = x_cord_contour(contours), reverse = False)

    (cnts, boundingBoxes) = contours.sort_contours(cnts, method="top-to-bottom")
    clone = image.copy()

    # Loop over the contours
    # for (i, c) in enumerate(contours)
    # for c in contours:
    
    for c in cnts:
        # computing bounding box for rectangle
        (x, y, w, h) = cv2.boundingRect(c)
        
        if w >=17 and h >=17:
            roi = blurred[y:y +h, x:x + w]
            ret, roi = cv2.threshold(roi, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            # roi = int(roi)
            squared = makeSquare(roi)
            final = resize_to_pixel(28, squared)
            l = str(a)
            cv2.imshow("final", final)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite("./Detected/img_"+l+".jpg",final)
            a= a + 1
            #cv2.waitKey(0)

print (datetime.now() - start_time)