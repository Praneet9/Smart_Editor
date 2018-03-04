import cv2
from imutils import contours
import imutils

original_image = cv2.imread('a.jpg')
#cv2.imshow('Original', original_image)
# cv2.waitKey(0)

original_image = cv2.resize(original_image, None, fx=0.3, fy=0.3)
cv2.imshow('Resized', original_image)
cv2.waitKey(0)

later = original_image.copy()

gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow('Gray', blurred)
cv2.waitKey(0)

ret, thresh = cv2.threshold(
    blurred, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)

edged = cv2.Canny(thresh, 30, 150)
cv2.imshow('Edges', edged)
cv2.waitKey(0)

ret, cnts, hierarchy = cv2.findContours(
    edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
(cnts, boundingBoxes) = contours.sort_contours(cnts, method="top-to-bottom")
clone = original_image.copy()

x_pnt = []
y_pnt = []
w_pnt = []
h_pnt = []
largest_h = 12
smallest_x = 0
smallest_y = 0
for c in cnts:
    # computing bounding box for rectangle
    (x, y, w, h) = cv2.boundingRect(c)

    if w >= 12 and h >= 12:
        roi = blurred[y:y + h, x:x + w]
        x_pnt.append(x)
        y_pnt.append(y)
        w_pnt.append(w)
        h_pnt.append(h)
        '''
		cv2.rectangle(img_scaled, (x,y), (x+w,y+h), (0,255,0), 5)
		cv2.imshow("rectangle", img_scaled)
		cv2.waitKey(0)
		'''
        ret, roi = cv2.threshold(
            roi, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


points = len(x_pnt)
# print(x_pnt,y_pnt,w_pnt,h_pnt)
largest_h = 12
smallest_x = x_pnt[0]
smallest_y = y_pnt[0]
largest_x = x_pnt[0]
x_pnt.append(x_pnt[-1])
y_pnt.append(y_pnt[-1])
w_pnt.append(w_pnt[-1])
h_pnt.append(h_pnt[-1])
for i in range(points):

    x, y, w, h = x_pnt[i], y_pnt[i], w_pnt[i], h_pnt[i]

    dumx, dumy = x, y
    if smallest_x > dumx:
        smallest_x = dumx
    if smallest_y > dumy:
        smallest_y = dumy
    if largest_x < dumx:
        largest_x = dumx
    if largest_h < h:
        largest_h = h

    if y_pnt[i + 1] > y + largest_h:
        # print(later.shape)
        # rint(x,y,w,h)
        cv2.rectangle(original_image, (smallest_x - w, smallest_y - h),
                      (largest_x + w, smallest_y + largest_h), (0, 0, 255), 5)
        cv2.imshow("rectangle", original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        smallest_x = x_pnt[i + 1]
        smallest_y = y_pnt[i + 1]
        #smallest_x = x_pnt[i + 1]
        cropped = later[smallest_y:smallest_y + largest_h, smallest_x:x + w]

"""
	if largest_h < h:
		largest_h = h
	if smallest_x > x:
		smallest_x = x
	if smallest_y > y:
		smallest_y = y
		"""
cv2.destroyAllWindows()


"""
tf.reset_default_graph()

model = Sequential()
model.add(Conv2D(30, (5,5), input_shape=(28,28,1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(15, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#TensorBoard Callback
tbcallback = TensorBoard(log_dir='./Graph', write_graph=True, write_images=True, histogram_freq=1)

model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=10, batch_size=200, callbacks=[tbcallback])
"""
