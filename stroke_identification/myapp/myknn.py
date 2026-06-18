import math
from tkinter import Tk, Label, Entry

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
# import pandas as pd
import random
from collections import Counter
# from sklearn import preprocessing
import time

#for plotting
from src.featureextract import glcm_feat


class CKNN:

    def __init__(self):
        self.accurate_predictions = 0
        self.total_predictions = 0
        self.accuracy = 0.0
        ##########
        with open('labels.dat') as f:
            lines = f.readlines()
        lines=[s.strip('\n') for s in lines]
        training_data=np.loadtxt("sample.data",dtype=float,delimiter=" ")
        # li=[1,9,2,3]
        # print((li[:-1]))




        self.training_set= { '1':[],'2':[]}
        test_set = {2: [], 4:[]}

        #Split data into training and test for cross validation
        #training_data = lbls[: len(lbls)]
        test_data = []#[-int(test_size * len(dataset)):]

        #Insert data into the training set
        cnt=0

        for record in training_data:
            st=lines[cnt][0]
            cnt+=1


            self.training_set[st[-1]].append( record[:])

    #########

    def predict(self,  to_predict, k = 1):
        # print(to_predict,training_data['6'][0])
        # if len(training_data) >= k:
        #     print("K cannot be smaller than the total voting groups(ie. number of training data points)")
        #     return

        distributions = []
        for group in self.training_set:
            i=0
            # print(group,'group')
            for features in self.training_set[group]:

                euclidean_distance = np.linalg.norm(np.array(features)- np.array(to_predict))
                if  group=='6':
                    # print('hi',euclidean_distance,training_data[group],len(training_data[group]),len(to_predict),i)
                    i+=1
                distributions.append([euclidean_distance, group])

        print(distributions)
        results = [i[1] for i in sorted(distributions)[:k]]
        result = Counter(results).most_common(1)[0][0]
        print("rs",results,self.training_set.keys())
        confidence = Counter(results).most_common(1)[0][1]/k

        return result, confidence



def prep(filename):

    #Insert data into the test set
    # for record in test_data:
    #print(len(training_set),len(training_set['1']),cnt)
    s = time.clock()
    feat=glcm_feat(filename)
    knn = CKNN()
    res=knn.predict(feat)#training_set['6'][1])
    print(res,"sruthi")
    e = time.clock()
    print("Exec Time:" ,e-s)
    # root=Tk()

    # p=Entry(root)
    # p.insert("Confidence is"+str(res[1]))
    # p.pack()
    #
    # root.mainloop()





    return res

# if __name__ == "__main__":
#     prep("C:\\Users\\sruthi\\Downloads\\Alzhe\\Alzhe\\src\\normal\\per6.jpg")

