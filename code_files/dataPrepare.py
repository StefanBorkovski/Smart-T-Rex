# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:54:24 2018

@author: Stefan Borkovski
"""

import numpy as np
import pandas as pd
from random import shuffle
from sklearn.preprocessing import MaxAbsScaler
import matplotlib

### se vcituva formiraniot data set ###

train_data = np.load('training_data.npy', allow_pickle = True)
df = pd.DataFrame(train_data)

Score = []
Distance = []
TRex_height = []
C1_height = []
C2_height = []
b_distance = []
b_height = []
Reaction = []

#### se formiraat nizi vo posakuvan format  ###

for i in range(len(df)):
    
    var = df[0][i][0]
    
    Score.append( var[0] )
    Distance.append( var[1] )
    TRex_height.append( 108 - var[2] ) 
    C1_height.append( var[3] )
    C2_height.append( var[4] )
    b_distance.append( var[5] )
    b_height.append( var[6] )
    if df[1][i] == [1,0]:    
        Reaction.append( 1 )
    else:
        Reaction.append( 0 )
        
#Score_n = [round(float(i)/max(Score),1) for i in Score]
#Distance_n = [round(float(i)/max(Distance),1) for i in Distance]
#TRex_height_n = [round(float(i)/max(TRex_height),1) for i in TRex_height]
#C1_height_n = [round(float(i)/max(C1_height),1) for i in C1_height]
#C2_height_n = [round(float(i)/max(C2_height),1) for i in C2_height]


scaler1 = max(Score)
#scaler2 = max(Distance)
#scaler3 = max(TRex_height)
#scaler4 = max(C1_height)
#scaler5 = max(C2_height)

###  so nizite se formira DataFrame-ot vo posakuvan format  ###

final_data = pd.DataFrame({'Score': Score, 'Distance': Distance, 'TRex_height': TRex_height, 'C1_height': C1_height, 'C2_height': C2_height, 'b_distance' : b_distance, 'b_height' : b_height, 'Reaction': Reaction  })


np.save('final_data', final_data)
    
#final_data.plot(kind='line');

