# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:25:03 2018

@author: Dell
"""

import numpy as np
import pandas as pd
from random import shuffle
from sklearn.preprocessing import MaxAbsScaler
import matplotlib
    
### se vcituva test data setot ###

test_data = np.load('test_data.npy')
    
test_df = pd.DataFrame(test_data)
    
Score = []
Distance = []
TRex_height = []
C1_height = []
C2_height = []
b_distance = []
b_height = []
Reaction = []

### se obrabotuvaat podatocite od data setot pri sto se formiraat nizi od parametri ###

for i in range(len(test_df)):
    var = test_df[0][i][0]
    var1 = test_df[1][i]
    
    Score.append( var[0] )
    Distance.append( var[1] )
    TRex_height.append( 108 - var[2] ) 
    C1_height.append( var[3] )
    C2_height.append( var[4] )
    b_distance.append( var[5] )
    b_height.append( var[6] )
    Reaction.append(var[0])
        
#Score_n = [round(float(i)/max(Score),1) for i in Score]
    
    
#Distance_n = [float(i)/max(Distance) for i in Distance]
#TRex_height_n = [float(i)/max(TRex_height) for i in TRex_height]
#C1_height_n = [float(i)/max(C1_height) for i in C1_height]
#C2_height_n = [float(i)/max(C2_height) for i in C2_height]
    
    
#scaler1 = max(Score)
    
#scaler2 = max(Distance)
#scaler3 = max(TRex_height)
#scaler4 = max(C1_height)
#scaler5 = max(C2_height)
    
### se formira DataFrame vo posakuvan format od kreiranite nizi ### 

final_test_data = pd.DataFrame({'Score': Score, 'Distance': Distance, 'TRex_height': TRex_height, 'C1_height': C1_height, 'C2_height': C2_height, 'b_distance' : b_distance, 'b_height' : b_height, 'Reaction': Reaction  })
    
    
np.save('final_test_data', final_test_data)
    
#final_test_data.plot(kind='line');