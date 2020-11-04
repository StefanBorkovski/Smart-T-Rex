 # -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:09:41 2018

@author: Dell
"""

from grabScreen import grab_screen
import cv2
import numpy as np
import pickle 
import time
from dataPrepare import scaler1
from directKeys import PressKey, ReleaseKey, UP, SPACE
import os
import pandas as pd

### reading objects from the game that will be detected ###

img_template1 = cv2.imread('cactus1.png',0)
img_template2 = cv2.imread('cactus2.png',0)
img_template3 = cv2.imread('bird.png',0)
trex = cv2.imread('t-rex.png',0)
img_restart = cv2.imread('restart.png',0)

### function for object detection ###

def match_template(screen, template,trs):
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = trs
    location = np.where( result >= threshold )
    try:    
        cv2.rectangle(screen, (location[1][0], location[0][0]), (location[1][0] + w, location[0][0]+h), (0,255,255), 1)
        flag = 1
    except:
        flag = 0

    try:
        loc_x=location[1][-1]
        loc_y=location[0][-1]
    except:
        loc_y = 0
        loc_x = 0
    return flag, loc_x, loc_y

### function for jump execution by sending SPACE command to the keyboard ###

def jump():
    PressKey(SPACE)
    time.sleep(0.15)
    ReleaseKey(SPACE)
 
### function for restarting the game when the dino is dead ###    
    
def restart():
    time.sleep(2) 
    PressKey(SPACE)
    print('Restart')
    ReleaseKey(SPACE)
    
### creation of file for keeping the parameters from the game (test set) ###

file_name = 'test_data.npy'

if os.path.isfile(file_name):
    print('file exist')
    test_data = list(np.load(file_name, allow_pickle = True))
else:
    print('file does not exist')
    test_data = []

def main():
   
    start_flag = 0
    flag_time = 0  
    distance = 0
    score = 0
    start_time = 0 
    current_time = 0
    
    ### loading the pretrained model ###
    
    filename='trained_model.sav'
    model = pickle.load(open(filename, 'rb'))
    
    while(True):  
    
        time1 = time.time() 
        
        ### detection of the objects ###
        
        screen=grab_screen(region=(120,350,370,500))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
        flag_c1, loc_x_c1, loc_y_c1 = match_template(screen, img_template1,0.7)
        flag_c2, loc_x_c2, loc_y_c2 = match_template(screen, img_template2,0.7)
        flag_t, loc_x_t, loc_y_t = match_template(screen, trex,0.9)
        flag_r, loc_x_r, loc_y_r = match_template(screen, img_restart,0.7)
        flag_b, loc_x_b, loc_y_b = match_template(screen, img_template3, 0.7)
          
        ### condition for starting the game ###    
        
        if  ( flag_c1 == 0 and flag_t == 1 and flag_r == 0 and flag_time == 0 ) :
            
            flag_time = 1
            start_flag = 1
            start_time = time.time()
                
        ### condition for stoping the game (when dino is dead) ###    
            
        if start_flag == 1 and flag_r == 1 :
            
            score = 0
            flag_time = 0
            start_flag = 0
           
            
            l = len(test_data) -1
            files = 0
            
            ### when the dino is dead delete the data around that period ###
            
            while (test_data[l][0])[0][1] != 0:
                del test_data[-1:]
                files = files + 1
                l = l - 1   
            print(" Last", files , "files have been deleted ")
            
            restart()
          
         ### evaluation of the distance from dino to the obstacles (cactuses and birds) ###
            
        if flag_time == 1 :
            try:    
                distance = loc_x_c1 + loc_x_c2 +loc_x_b - 24
                if distance < 0:
                    distance = 0
                  #distance = int( ( distance / 188)*100)
            except:
                distance = 0
              
        ### condition for point counting (increasing of the result) ###
                
        if start_flag == 1 :
            
            current_time = time.time()
        
            if(current_time - start_time > 1):
                start_time = time.time()
                current_time = 0
                score = score + 1
            
            print('Score:',int(score), 'Distance:',distance, 'T-Rex height',loc_y_t)
           
            ### creation of test vector ### 
            
            X_test = [round(score,1), distance, loc_y_t, loc_y_c1, loc_y_c2, loc_x_b, loc_y_b]
            
#            print(X_test)
             
            X_test = np.asarray( X_test ) 
            
            ### appending the result from the classifier to the decision array ###
            
            result = model.predict( X_test.reshape(1,-1) )
            results = []
            results.append(result)
#            print(result)
            
            ### if the result from the classifier is positive then jump ###
            
            if result == 1:
                jump()
                print(' Cactus in front of me ! ')
                
            ### appending the parameters to test array ###
            
            features = []
            features.append([score, distance, loc_y_t, loc_y_c1, loc_y_c2, loc_x_b, loc_y_b])
            
            test_data.append( [features, result] )

            
#            if len(test_data) % 100 == 0:
#                print(len(test_data))
#                np.save(file_name, pd.DataFrame(test_data))
        
###  showing the window from the game   ###          
        
        cv2.imshow('screen', screen)
            
        if cv2.waitKey(25) & 0xFF == ord('q'):
                
            cv2.destroyAllWindows()
            break
            
        time.sleep(0.02)
            
        time2 = time.time()
            
###   printing the time required for one frame (for synchronization)   ###
        
#        print("Time was {}:".format(time2-time1))

        
main()

