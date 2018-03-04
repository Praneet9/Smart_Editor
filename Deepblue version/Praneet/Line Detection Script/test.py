import cv2
import numpy as np
from pprint import pprint
#import image
image = cv2.imread('vrkIj.png')
c = image.copy()
#image = cv2.resize(image, None, fx=0.2, fy=0.2)

# cv2.imshow('orig',image)
# cv2.waitKey(0)

# grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#pprint(gray, indent=2)

# print(str(gray))
#cv2.imshow('gray', gray)
# cv2.waitKey(0)

# binary
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow('second', thresh)
# cv2.waitKey(0)

# dilation
kernel = np.ones((10, 80), np.uint8)
# original values 5,100
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#cv2.imshow('dilated', img_dilation)
# cv2.waitKey(0)

# find contours
im2, ctrs, hier = cv2.findContours(
    img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])
i = 1
cropped_images = []
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    dimensions = [x, y, w, h]
    # Getting ROI
    roi = c[y:y + h, x:x + w]
    cropped_images.append(dimensions)
    #cv2.imwrite('test' + str(i) + '.jpg', roi)
    i += 1
    # show ROI

    #cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image, (x, y), (x + w, y + h), (90, 0, 255), 2)
    # cv2.waitKey(0)

#cv2.imshow('marked areas', image)
# cv2.waitKey(0)
# print(cropped_images)
j = 1
for x, y, w, h in cropped_images:
    img = c[y:y + h, x:x + w]
    d = img.copy()
    #cv2.imwrite('test' + str(j) + '.jpg', img)
    j += 1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('orig', gray)
    # cv2.waitKey(0)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    #cv2.imshow('orig', thresh)
    # cv2.waitKey(0)
    kernel = np.ones((10, 15), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imshow('orig', img_dilation)
    cv2.waitKey(0)
    im2, ctrs, hier = cv2.findContours(
        img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    i = 1
    cv2.destroyAllWindows()
    images = []
    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
        # Getting ROI
        roi = d[y:y + h, x:x + w]

        # cv2.imshow('test', roi)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite('test' + str(i) + '.jpg', roi)
        new_image = cv2.imread('test' + str(i) + '.jpg')
        gray = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((10, 1), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)
        cv2.imshow('dilation', img_dilation)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        im2, ctrs, hier = cv2.findContours(
            img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        e = thresh.copy()
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

        for i, ctr in enumerate(sorted_ctrs):
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)
            #dimensions = [x, y, w, h]
            # Getting ROI
            roi = e[y:y + h, x:x + w]
            cv2.imshow('test', roi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # cropped_images.append(dimensions)
            #cv2.imwrite('test' + str(i) + '.jpg', roi)
            #i += 1
            # show ROI

            #cv2.imshow('segment no:'+str(i),roi)
            #cv2.rectangle(image, (x, y), (x + w, y + h), (90, 0, 255), 2)

        # for x_new, y_new, w_new, h_new in roi
        # cv2.imwrite('test' + str(i) + '.jpg', roi)
        #images.append([x, y, w, h])
        i += 1

# for x, y, w, h in images:
#     cv2.imshow('test', d[y:y + h, x:x + w])
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
