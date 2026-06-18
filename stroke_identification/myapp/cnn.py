# coding: utf-8

# In[ ]:

from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D


from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np

#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =10
batch_size =150
epochs = 40
#------------------------------

import os, cv2, keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2

# Data Import
def read_dataset():
    data_list = []
    label_list = []
    i=-1
    my_list = os.listdir(r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Train')
    for pa in my_list:
        i=i+1
        print(pa,"==================")
        for root, dirs, files in os.walk(r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Train\\' + pa):

         for f in files:
            file_path = os.path.join(r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Train\\'+pa, f)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            res = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
            data_list.append(res)


            label_list.append(i)
            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))

def read_dataset1(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))

from sklearn.model_selection import train_test_split

# load dataset
x_dataset, y_dataset = read_dataset()
print(x_dataset.shape)

n_samples,depth, height = x_dataset.shape


x_dataset_reshaped = x_dataset.reshape(n_samples, depth * height )


from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state = 2)
X_train_res, y_train_res = sm.fit_resample(x_dataset_reshaped, y_dataset)
print('After OverSampling, the shape of train_X: {}'.format(x_dataset_reshaped.shape))
print('After OverSampling, the shape of train_y: {} \n'.format(y_train_res.shape))
print("After OverSampling, counts of label '1': {}".format(sum(y_train_res == 1)))
print("After OverSampling, counts of label '0': {}".format(sum(y_train_res == 0)))
X_train_res_3d = X_train_res.reshape(-1, depth, height)
print("============================================")
print("============================================")
print("============================================")
print("============================================")
X_train, X_test, y_train, y_test = train_test_split(X_train_res_3d, y_train_res, test_size=0.2, random_state=0)

y_train1=[]
for i in y_train:
    conv = keras.utils.to_categorical(i, num_classes)

    y_train1.append(conv)

y_train=y_train1
x_train = np.array(X_train, 'float32')
y_train = np.array(y_train, 'float32')
x_test = np.array(X_test, 'float32')
y_test = np.array(y_test, 'float32')

x_train /= 255  # normalize inputs between [0, 1]
x_test /= 255

print("x_train.shape",x_train.shape)
x_train = x_train.reshape(x_train.shape[0], 64,64, 1)
x_train = x_train.astype('float32')
x_test = x_test.reshape(x_test.shape[0], 64,64, 1)
x_test = x_test.astype('float32')

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
# ------------------------------

# construct CNN structure

model = Sequential()

# 1st convolution layer
model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(64, 64, 1)))
model.add(MaxPooling2D(pool_size=(5, 5), strides=  (2, 2)))

# 2nd convolution layer
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

# 3rd convolution layer
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

model.add(Flatten())

# fully connected neural networks
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_classes, activation='softmax'))
# ------------------------------
# batch process

print(x_train.shape)

gen = ImageDataGenerator()
train_generator = gen.flow(x_train, y_train, batch_size=batch_size)

# ------------------------------

model.compile(loss='categorical_crossentropy'
              , optimizer=keras.optimizers.Adam()
              , metrics=['accuracy']
              )

# ------------------------------

if not os.path.exists("model1.h5"):

    model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)
    model.save("model1.h5")  # train for randomly selected one
else:
    model = load_model("model1.h5")  # load weights


yp=model.predict_classes(x_test,verbose=0)
print(yp)
print(y_test)

from sklearn.metrics import classification_report
# target_names=os.listdir(r'D:\python code\archive\Project')
print(classification_report(y_test, yp))