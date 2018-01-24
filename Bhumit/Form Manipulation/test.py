import cv2
import numpy as np 

# Read blank form
form = cv2.imread('simpleform.jpg', cv2.IMREAD_GRAYSCALE)
form = np.array(form)
#form = cv2.GaussianBlur(form, (5,5), 0)
form = cv2.threshold(form, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('Form', form)
cv2.waitKey(0)
# cv2.destroyAllWindows()

fill_form = cv2.imread('simpleformfill.jpg', cv2.IMREAD_GRAYSCALE)
fill_form = np.array(fill_form)
#fill_form = cv2.GaussianBlur(fill_form, (5,5), 0)
fill_form = cv2.threshold(fill_form, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('Filled Form', fill_form)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# Subtracting fill_form - form to get the difference fields in images of the form
result = np.subtract(fill_form, form)
# Applying Inverse Thresholding to get white background
result = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()