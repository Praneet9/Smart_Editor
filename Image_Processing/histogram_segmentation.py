import cv2
import numpy as np

img = cv2.imread('img.jpg', 0)
imge = cv2.imread('imgeroded.jpg', 0)

print(img.shape)
col_histo_width = img.shape[1]
col_histo_height = img.shape[0]
col_histogram = np.zeros((col_histo_height, col_histo_width), np.uint8)

# Initializing horizontal histogram
row_histo_height = img.shape[0]
row_histo_width = img.shape[1]
row_histogram = np.zeros((row_histo_height, row_histo_width), np.uint8)

# Calculating horizontal histogram
#row_histo_width = 0
# rowsums = []
# for row in range(row_histo_height):
#     running_sum = sum(img[row, :]) // 255
#     rowsums.append(running_sum)
#     #row_histogram[row, :running_sum] = 255
#     #if running_sum > row_histo_width:
#     #   row_histo_width = running_sum
# # cut off the histogram image where histo ends
# #row_histogram = row_histogram[:, :row_histo_width]
# print("Row sums are : ")
# print(rowsums)
def cropImage(start, end):
	character = imge[:, start:end]
	cv2.imwrite('img_' + str(start) + str(end) + '.jpg', character)

colsums = []
startflag = False
endflag = True
for col in range(col_histo_width):
    running_sum = sum(img[:, col]) // 255
    if startflag == False and running_sum >= 20:
    	startindex = col
    	if (startindex < 0):
    		startindex = 0
    	startflag = True
    	endflag = False
    if endflag == False and running_sum <= 20:
    	endindex = col
    	if endindex > col_histo_width:
    		endindex = col_histo_width
    	endflag = True
    	startflag = False
    	if startindex != endindex:
	    	cropImage(startindex, endindex)
    colsums.append(running_sum)

print("Column sums are : ")
print(colsums)