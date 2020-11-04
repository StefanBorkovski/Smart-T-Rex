# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:32:24 2018

@author: Stefan Borkovski 
"""

from sklearn.neighbors import KNeighborsClassifier

import numpy as np
import pickle

### se vcituva data setot ###

train_data = np.load('final_data.npy')

### podelba na datasetot na train i test mnozestva ###

X_train = train_data[:,0:7]
y_train = train_data[:,-1]

### se formira model na Klasifikator ###

model =KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=3, metric='minkowski', metric_params=None, n_jobs=None)

### se trenira modelot so formiraniot data set ###

model.fit(X_train, y_train) 

### se zacuvuva treniraniot model ###

filename = 'trained_model.sav'
pickle.dump(model, open(filename, 'wb'))

