import tensorflow as tf
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

import keras

from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.utils import to_categorical
from keras.optimizers import SGD, RMSprop, adadelta, Adam

from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint

from sklearn.model_selection import train_test_split

PATH = os.getcwd()
data_path = './Dataset'
#data_Dir_list = os.listdir(data_path)
data_Dir_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'q', 'r', 't', 'y', '_A',
                 '_B', '_C', '_D', '_E', '_F', '_G', '_H', '_I', '_J', '_K', '_L', '_M', '_N', '_O', '_P', '_Q', '_R', '_S', '_T', '_U', '_V', '_W', '_X', '_Y', '_Z']
print(data_Dir_list)
img_row = 28
img_col = 28
num_channel = 1
epoch = 500
num_classes = 52

img_data_list = []
images = []
i = 0

for dataset in data_Dir_list:
    img_list = os.listdir(data_path + '/' + dataset)
    for img in img_list:
        i = i + 1
        ip_img = cv2.imread(data_path + '/' + dataset + '/' + img)
        ip_img = cv2.cvtColor(ip_img, cv2.COLOR_BGR2GRAY)
        ip_img = cv2.resize(ip_img, (img_row, img_col))
        img_data_list.append(ip_img)
    images.append(i)

print(images)

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255
img_data.shape

img_data = np.expand_dims(img_data, axis=4)
img_data.shape

# Preprocessing
n_samples = img_data.shape[0]
labels = np.ones((n_samples,), dtype='int64')

"""label_dictionary = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 'a':'a', 'b':'b', 'c':'c',
                    'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n',
                    'o':'o', 'p':'p', 'q':'q', 'r':'r'}"""
#from numpy import argmax

labels[:images[0]] = data_Dir_list.index(data_Dir_list[0])
label_dictionary = {}
label_dictionary[0] = data_Dir_list[0]

count = 0
for class_name in data_Dir_list:
    if count == 0:
        count += 1
        continue
    else:
        labels[images[count - 1]:images[count]
               ] = data_Dir_list.index(class_name)
        label_dictionary[count] = class_name
        count += 1

# One-Hot encoded format
Y = to_categorical(labels, num_classes)
#Y = argmax(Y)
print(label_dictionary)

# Shuffle data
from sklearn.utils import shuffle
x, y = shuffle(img_data, Y, random_state=2)
# Split Dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.20, random_state=2)

datagen = ImageDataGenerator(
    featurewise_center=False,  # set input mean to 0 over the dataset
    samplewise_center=False,  # set each sample mean to 0
    shear_range=0.2,
    zoom_range=0.2,
    featurewise_std_normalization=False,  # divide inputs by std of the dataset
    samplewise_std_normalization=False,  # divide each input by its std
    zca_whitening=False,  # apply ZCA whitening
    # randomly rotate images in the range (degrees, 0 to 180)
    rotation_range=15,
    # randomly shift images horizontally (fraction of total width)
    width_shift_range=0.2,
    # randomly shift images vertically (fraction of total height)
    height_shift_range=0.2,
    horizontal_flip=False,  # randomly flip images
    vertical_flip=False)  # randomly flip images

datagen.fit(X_train)

tf.reset_default_graph()
model = Sequential()
model.add(Conv2D(32, (3, 3), strides=(1, 1),
                 activation='relu', input_shape=(img_row, img_col, 1)))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(64, (3, 3), strides=(1, 1), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(312, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(52, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.summary()

augmented_checkpoint = ModelCheckpoint('augmented_best_model.hdf5',  # model filename
                                       monitor='val_loss',  # quantity to monitor
                                       verbose=1,  # verbosity - 0 or 1
                                       save_best_only=True,  # The latest best model will not be overwritten
                                       mode='auto')  # The decision to overwrite model is made
# automatically depending on the quantity to monitor

model.compile(loss=keras.losses.categorical_crossentropy,  # Better loss function for neural networks
              optimizer=keras.optimizers.Adam(),  # Adam optimizer with 1.0e-4 learning rate
              metrics=['accuracy'])  # Metrics to be evaluated by the model

hist = model.fit_generator(datagen.flow(X_train, Y_train, batch_size=250),  # number of samples per gradient update
                           epochs=epoch,  # number of iterations
                           validation_data=(X_test, Y_test),
                           callbacks=[augmented_checkpoint],
                           verbose=1,
                           shuffle=True)

import pickle

with open('./model/history', 'wb') as file_pi:
    pickle.dump(hist.history, file_pi)

model.save('./model/model.hdf5')
