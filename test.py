# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:09:25 2018

@author: Dell
"""
from grabScreen import grab_screen
import cv2

while(True):
    
    screen=grab_screen(region=(120,350,370,500))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('screen', screen)
             
    if cv2.waitKey(25) & 0xFF == ord('q'):             
        cv2.destroyAllWindows()
        break
