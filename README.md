# Functions that are used in this work will be explained here:
## AUXILARY FUNCTIONS:
---
### “getKeys.py” 
> This code is used for reading the commands from the computer keyboard while creating the data set. It is used to get human actions while playing the game.
### “grabScreen.py”

> This code is used for taking frames from the screen, but not from the whole screen. Only part of the screen that captures the Dino and the first obstacles is taken. The adjustment is made to capture the Dino and the first obstacle that appears. Also, this code is used to get object information from the game through object detection.
### “directKeys.py”
> This code is used for executing the commands from the code into the game window.
##  MAIN FUNCTIONS:
---
### “getData.py”
> This code is used for creating the data set.
### “dataPrepare.py”
> This code is used for preprocessing the data and reforming the data into data frames.
### “training_KNN_Classifier.py”
> This code is used for creating a classifier from collected data
## MAIN ALGORITHM:
---
### “testing_KNN_Classifier.py”
> This code is merging all the functions that enable collecting data in real-time, putting data across the classifiers, generating decisions, and acting in the game window.
## INSTRUCTIONS: 
---
> If the one wants to create its data set for training from scratch it must examine all functions in the specified order. If the one wants only to test the algorithm, there is available data and trained models which are ready to be used (so the main code can be used straight away).
##  CODE FOR DATA ANALYSIS (as a time series):
---
### “test_data_Prepare.py”
> This code enables graphical visualization of the features and reactions from training and test data set as time-series data. 


Before creating a data set or testing the previously created model some parameters must be adjusted!!!
### “test.py”
> This is a code for adjusting the size of the window that “getScreen.py” will capture. The window should be adjusted so only the Dino is visible on the left side and the first obstacle on the right side of the window. As an example, one can use “Example.jpg”. After the window parameters are obtained from the “test.py” code they should be copied to “testing_KNN_Classifier.py”. From the 12th line of code from “test.py”, the region parameters should be copied to the 96th line of code in “testing_KNN_Classifier.py”.
##  RECOMENDATIONS: 
---
> **-The game can be played on the following website: [T-Rex game](http://www.trex-game.skipser.com/). You should tilt the window from python on the right part of the screen and the window from the web browser on the left part of the screen! An Ad-Blocker should be used because pop-up ads can overwrite the game window. Spyder is recommended. The virtual environment created through anaconda can be found in the “trex_env” folder.**

