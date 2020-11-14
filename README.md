# Smart T-Rex: Project Explanation

Smart T-Rex is a machine-learning-based algorithm that enables autonomous playing of the T-Rex game. The solution is based on the k-nearest neighbors classifier. The first part of the solution is creating the data set. Data set is created from a human play. To improve the training process the unwanted data which presents the death of the T-Rex is not used in the creation of the data set. The created data set is caring information from human actions like distance before jump and features of the faced obstacles. The play is evaluated and rewarded every second while the one is playing by adding one point to the Score sum.\
The created raw data set needs further processing. The first step is to be split into test data and train data. Then the data is reformed into data frames that are a perfect fit for the classifier. In this part of processing, the default value is set for the height of the Dino as zero. In other words, the default Dino pose is calibrated at zero height. After processing both data sets it is time for training.

The default values for the hyperparameters of the classifiers are used because of the simplicity of the task. The trained model, after every training, is saved as a new model for further use and evaluation. While testing the model in real-time data is collected from the game and passed to the classifier. Then the output of the classifier is applied to the computer machine as a corresponding action. If the output is positive, then the computer performs the jump command (hopefully the obstacle is avoided).

In the testing process, gathered data contain features and actions which are then packed into the test data set which is used for graphic visualization, so we will be able to compare the human action versus algorithm action.

The process of data collection is enabled by functions that locate a small predefined part of the screen (where the Dino and obstacles are appearing) and detect the objects of interest. After the objects are allocated the next step is measuring the height of the obstacle and distance between the Dino and the obstacle. The game window must be visible for the user all the time so it will be for the algorithm too. While data is gathered for training and testing the frames per second parameter must be synchronized. This is very important because if these two parameters are not synchronized the actions may be delayed or taken before. After the death of the Dino if the user starts to play again the new data is concatenated to the old one to expand the training data set. The k-nearest neighbors classifier requires just a few rounds of the game to be played so it can imitate a human playing.

** **This work is done with the possibility to be expanded in the generative model which will be able to expand the knowledge base and improve the score in every play on its own.**

▸ This work is done as a project for faculty subject "Machine learning". November 2018.

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

