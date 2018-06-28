import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import os
from datetime import datetime


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
        doublesize = cv2.resize(
            not_square, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
        height = height * 2
        width = width * 2
        if (height > width):
            pad = (height - width) / 2
            pad = int(pad)
            #doublesize = int(doublesize)
            doublesize_square = cv2.copyMakeBorder(doublesize, 0, 0, pad,
                                                   pad, cv2.BORDER_CONSTANT, value=BLACK)
        else:
            pad = (width - height) / 2
            pad = int(pad)
            doublesize_square = cv2.copyMakeBorder(doublesize, pad, pad, 0, 0,
                                                   cv2.BORDER_CONSTANT, value=BLACK)
    doublesize_square_dim = doublesize_square.shape
    return doublesize_square


def resize_to_pixel(dimensions, image):

    buffer_pix = 4
    dimensions = dimensions - buffer_pix
    squared = image
    r = float(dimensions) / squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    widht_r = img_dim2[1]
    BLACK = [0, 0, 0]
    if (height_r > widht_r):
        resized = cv2.copyMakeBorder(
            resized, 0, 0, 0, 1, cv2.BORDER_CONSTANT, value=BLACK)
    if (height_r < widht_r):
        resized = cv2.copyMakeBorder(
            resized, 1, 0, 0, 0, cv2.BORDER_CONSTANT, value=BLACK)
    p = 2
    ReSizedImg = cv2.copyMakeBorder(
        resized, p, p, p, p, cv2.BORDER_CONSTANT, value=BLACK)
    img_dim = ReSizedImg.shape
    height = img_dim[0]
    width = img_dim[1]
    return ReSizedImg


start_time = datetime.now()

THRESHOLD = 0.01
base_directory = './cropped_images/'
total_files = len(glob.glob('./cropped_images/*.jpg'))

characters = []
dataframe = pd.read_csv('./first_and_last_names.csv')
dataframe = dataframe.dropna(subset=['transcription'])
total_names = dataframe.iloc[0:total_files, :-1]
for i, name in enumerate(total_names['transcription']):
    characters.append(list(name))

for i in range(total_files):
    if i == 4096 or i == 4097:
        continue
    img = cv2.imread('./cropped_images/img_' + str(i) + '.jpg', 0)
    img = cv2.bitwise_not(img)
    try:
        # Initializing vertical histogram
        col_histo_width = img.shape[1]
        col_histo_height = 200
        col_histogram = np.zeros((col_histo_height, col_histo_width), np.uint8)

        # Initializing horizontal histogram
        row_histo_height = img.shape[0]
        row_histo_width = 400
        row_histogram = np.zeros((row_histo_height, row_histo_width), np.uint8)

        # Calculating horizontal histogram
        row_histo_width = 0
        for row in range(row_histo_height):
            running_sum = sum(img[row, :]) // 255
            row_histogram[row, :running_sum] = 255
            if running_sum > row_histo_width:
                row_histo_width = running_sum
        # cut off the histogram image where histo ends
        row_histogram = row_histogram[:, :row_histo_width]

        # calculating bounding indexes for rows using the histogram
        all_digit_rects = []
        line_rects = []
        starting_idx = False
        for j in range(row_histo_height):
            thresholded_idx = int(THRESHOLD * row_histo_width)
            if row_histogram[j, thresholded_idx] == 255 and not starting_idx:
                starting_idx = j
            elif row_histogram[j, thresholded_idx] != 255 and starting_idx != False:
                last_idx = j
                if abs(starting_idx - last_idx) > 1:
                    line_rects.append((starting_idx, last_idx))
                starting_idx = False

        if len(line_rects) == 0:
            line_rects.append((0, row_histo_height))

        for idx, line_rect in enumerate(line_rects):
            line = img[line_rect[0]:line_rect[1], :]

            # Initializing vertical histogram
            col_histo_width = img.shape[1]
            col_histogram = np.zeros(
                (col_histo_height, col_histo_width), np.uint8)

            # calculating vertical histogram for current row
            col_histo_height = 0
            for column in range(col_histo_width):
                running_sum = sum(line[:, column]) // 255
                col_histogram[:running_sum, column] = 255
                if running_sum > col_histo_height:
                    col_histo_height = running_sum
            col_histogram = col_histogram[:col_histo_height, :]

            # calculating bounding boxes for each digit
            digit_rects = []
            starting_idx = False
            for j in range(col_histo_width):
                thresholded_idx = int(THRESHOLD * col_histo_height)
                if col_histogram[thresholded_idx, j] == 255 and not starting_idx:
                    starting_idx = j
                elif col_histogram[thresholded_idx, j] != 255 and starting_idx != False:
                    last_idx = j
                    if abs(starting_idx - last_idx) > 1:
                        digit_rects.append((starting_idx, last_idx))
                    starting_idx = False
            for digit in digit_rects:
                all_digit_rects.append(
                    (line_rect[0], line_rect[1], digit[0], digit[1]))

        col_histogram = cv2.bitwise_not(col_histogram)
        row_histogram = cv2.bitwise_not(row_histogram)

        word = characters[i]
        mat_size = math.ceil(math.sqrt(len(all_digit_rects)))
        if len(word) == len(all_digit_rects):
            for idx, digit in enumerate(all_digit_rects):
                current_character = img[all_digit_rects[idx][0]:all_digit_rects[idx]
                                        [1], all_digit_rects[idx][2]:all_digit_rects[idx][3]]
                if not os.path.exists(word[idx]):
                    os.makedirs(word[idx])
                squared = makeSquare(current_character)
                size28 = resize_to_pixel(28, squared)
                cv2.imwrite(
                    './' + str(word[idx]) + '/' + str(i) + '.jpg', size28)
        i += 1
    except:
        print('\n\nError in Image {0}\n\n'.format(i - 1))
        continue
end_time = datetime.now()
print('Processded {0} images in {1} seconds'.format(
    total_files, end_time - start_time))
