# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:32:44 2018

@author: Stefan Borkovski
"""

from getKeys import key_check
from grabScreen import grab_screen
import cv2
import numpy as np
import os
import time 

### vcituvanje na objektite za detekcija ###

img_template1 = cv2.imread('cactus1.png',0)
img_template2 = cv2.imread('cactus2.png',0)
img_template3 = cv2.imread('bird.png',0)
trex = cv2.imread('t-rex.png',0)
img_restart = cv2.imread('restart.png',0)

### match_template pretstavuva funkcijaa koja ovozmozuva detekcija na objektite od interes ###

def match_template(screen, template, trs):
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

def keys_to_output(keys):
    #[ ,nothing]
    output = [0, 0]
    
    if ' ' in keys:
        output[0] = 1
    else:
        output[1] = 1
        
    return output

### se kreira podatok vo koj sto ke se smestuvaat parametrite  ###
      
file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('file exist')
    training_data = list(np.load(file_name))
else:
    print('file does not exist')
    training_data = []


def main():
   
    start_flag = 0
    flag_time = 0
    distance = 0
    score = 0
    start_time = 0
    current_time = 0
    
    while(True):  
    
#        time1 = time.time()
		
		### se vrsi lociranje(detekcija) na objektite ###
        
        screen=grab_screen(region=(110,290,370,450))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
        flag_c1, loc_x_c1, loc_y_c1 = match_template(screen, img_template1, 0.7)
        flag_c2, loc_x_c2, loc_y_c2 = match_template(screen, img_template2, 0.7)
        flag_t, loc_x_t, loc_y_t = match_template(screen, trex, 0.9)
        flag_r, loc_x_r, loc_y_r = match_template(screen, img_restart, 0.7)
        flag_b, loc_x_b, loc_y_b = match_template(screen, img_template3, 0.7)
           
        ### uslov za pocetok na igrata  ###
            
        if  ( flag_c1 == 0 and flag_t == 1 and flag_r == 0 and flag_time == 0 ) :
            
            flag_time = 1
            start_flag = 1
            start_time = time.time()
         
		### uslov koj oznacuva kraj na zivotot na dinosaurusot ###
		 
        if start_flag == 1 and flag_r == 1 :
            
            score = 0
            flag_time = 0
            start_flag = 0
            
            l = len(training_data) -1
            files = 0
            
			### koga dinosaurusot ke go izgubi zivotot se brisat podatocite koi go oznacuvaat ovoj nastan ###
			
            while (training_data[l][0])[0][1] != 0:
                del training_data[-1:]
                files = files + 1
                l = l - 1   
            print(" Last", files , "files have been deleted ")
			
		### uslov preku koj se odreduva rastojanieto do preprekite(kaktusite i pticata) ###
                
        if flag_time == 1 :
            try:    
                distance = loc_x_c1 + loc_x_c2 +loc_x_b - 24
                if distance < 0:
                    distance = 0
                #distance = int( ( distance / 188)*100)
            except:
                distance = 0
                
		### uslov za pocetok na startuvnje na broenje (zgolemuvanje za postignatiot rezultat) ###
		
        if start_flag == 1 :
            
            current_time = time.time()
        
            if(current_time - start_time > 1):
                start_time = time.time()
                current_time = 0
                score = score + 1
            
#            print('Score:',int(score), 'Distance:',distance, 'T-Rex height',loc_y_t)

			### se otcituva pritisnato kopce i se pridava kon mnozestvo na reakcija ###
            ### se dodavaat parametrite kon data setot ###
                
            keys = key_check()
            output = keys_to_output(keys)  
            features = []
            features.append([score, distance, loc_y_t, loc_y_c1, loc_y_c2, loc_x_b, loc_y_b])
            training_data.append([features,output])
              
			### se vrsi zacuvuvanje na podatokot ### 
                  
            if len(training_data) % 100 == 0:
                print(len(training_data))
                np.save(file_name,training_data)
        
### prikazuvanje na detekcijata vo definiranata ramka      ###   
		
#        cv2.imshow('screen', screen)
#             
#        if cv2.waitKey(25) & 0xFF == ord('q'):
#                
#            cv2.destroyAllWindows()
#            break

        time2 = time.time() 

### se pecati vremeto potrebno za eden frame za ponatamosna sinhronizacija   #### 		
            
#        print("Time was {}:".format(time2-time1))
            
main()




      

