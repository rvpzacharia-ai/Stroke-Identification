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


def read_dataset1(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]r

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))



def predictfn(path):
    res=read_dataset1(path)
    model = load_model(r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\model1.h5")


    res /= 255  # normalize inputs between [0, 1]

    my_list = os.listdir(r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Train')

    res = res.reshape(res.shape[0], 64, 64, 1)
    r=model.predict_classes(res,verbose=0)
    return my_list[r[0]]

