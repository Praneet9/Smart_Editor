import cv2
import numpy as np
from imutils import contours
import imutils

# Read blank form
form = cv2.imread('./test_images/nonfilled_300.jpeg', cv2.IMREAD_GRAYSCALE)
form = np.array(form)
# form = cv2.GaussianBlur(form, (5,5), 0)
form = cv2.threshold(
    form, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
form = cv2.dilate(form, np.ones((3, 3), np.uint8), iterations=1)
cv2.imshow('Form', form)
cv2.waitKey(0)
# cv2.destroyAllWindows()

fill_form = cv2.imread(
    './test_images/filled_300.jpeg', cv2.IMREAD_GRAYSCALE)
fill_form = np.array(fill_form)
# fill_form = cv2.GaussianBlur(fill_form, (5,5), 0)
fill_form = cv2.threshold(
    fill_form, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#fill_form = cv2.dilate(fill_form, np.ones((2, 2), np.uint8), iterations=1)
#fill_form = cv2.erode(fill_form, np.ones((2, 2), np.uint8), iterations=1)

cv2.imshow('Filled Form', fill_form)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# Subtracting fill_form - form to get the difference fields in images of the form
result = np.subtract(fill_form, form)
# Applying Inverse Thresholding to get white background
result = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY)[1]
result_copy = result.copy()
result = cv2.erode(result, np.ones((3, 3), np.uint8), iterations=1)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.imwrite('testing.jpg', result)
result = cv2.dilate(result, np.ones((2, 2), np.uint8), iterations=1)
result = cv2.bitwise_not(result)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.imwrite('testing.jpg', result)


edged = cv2.Canny(result, 30, 150)
cv2.imshow('Edges', edged)
cv2.waitKey(0)
kernel = np.ones((1, 10), np.uint8)
edged = cv2.dilate(edged, kernel, iterations=1)
cv2.imshow('Edges', edged)
cv2.waitKey(0)
# Find contours
# ret, cnts, hierarchy = cv2.findContours(
#     edged.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# (cnts, boundingBoxes) = contours.sort_contours(cnts, method="left-to-right")
# (cnts, boundingBoxes) = contours.sort_contours(cnts, method="top-to-bottom")
# a = 1
# for c in cnts:
#     # computing bounding box for rectangle
#     (x, y, w, h) = cv2.boundingRect(c)
#     #print("Area = " + str(w * h) + " No constraints")
#     if w * h > 115:
#         #print("Area = " + str(w * h) + " Constraints")
#         roi = ""
#         roi = result_copy[y:y + h, x:x + w]
#         ret, roi = cv2.threshold(
#             roi, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         # roi = int(roi)
#         # squared = makeSquare(roi)
#         # final = resize_to_pixel(28, squared)
#         l = str(a)
#         cv2.imshow("final", roi)
#         cv2.waitKey(0)
#         # roi = ""
#         #cv2.imwrite("img_" + l + ".jpg", roi)
#         a = a + 1
#         # cv2.waitKey(0)

cv2.destroyAllWindows()
