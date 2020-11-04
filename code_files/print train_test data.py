# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:09:18 2018

@author: Dell
"""
import numpy as np
import pandas as pd

### se vrsi vcituvanje na test i train setovi i nivno graficko prikazuvanje ###

final_data = np.load('final_data.npy')
final_train_data = pd.DataFrame(final_data)
final_train_data = final_train_data.rename(index=str, columns={0:'Score',1: 'Distance',2: 'TRex_height', 3:'C1_height',4: 'C2_height' ,5:'b_distance' ,6: 'b_height' ,7: 'Reaction' })

final_test_data = np.load('final_test_data.npy')
final_test_data = pd.DataFrame(final_test_data)
final_test_data = final_test_data.rename(index=str, columns={0:'Score',1: 'Distance',2: 'TRex_height', 3:'C1_height',4: 'C2_height' ,5:'b_distance' ,6: 'b_height' ,7: 'Reaction' })

final_train_data.plot(kind='line', title = 'train_data');

final_test_data.plot(kind='line', title = 'test_data');

