# Project Name : Emotion-recognition
# Table of Content :

1.[Description](#p1)

2.[Dependencies](#p2)

3.[Usage](#p3)

4.[Acknowledgements](#p4)

<a id="p1"></a> 
# Description:

Human faces have many emotions, this project looks at using these to create a unique password to protect important files. Facial emotion is first classified using a classifier originally found here: [https://github.com/omar178/Emotion-recognition](https://github.com/omar178/Emotion-recognition). By specifying the number of emotions to use, the system will return an array of the specified number of emotions registered from the user. For example, if `hack5.py 3 1` was used to run the program, the system would return an array of 3 emotions measured as 1 second each. This returned array is then passed through an SHA-2 256 bit hash algorithm to create a password which is output to the terminal. 

This password is unique to the emotions shown, the number of emotions, and even the duration specified for the emotions.

## What does Emotion Recognition mean?

Emotion recognition is a technique used in software that allows a program to "read" the emotions on a human face using advanced image processing. Companies have been experimenting with combining sophisticated algorithms with image processing techniques that have emerged in the past ten years to understand more about what an image or a video of a person's face tells us about how he/she is feeling and not just that but also showing the probabilities of mixed emotions a face could has. Our emotion recognition system was originally created by Omar Ayman here [https://github.com/omar178/Emotion-recognition](https://github.com/omar178/Emotion-recognition)

<a id="p2"></a> 
# Dependencies:
* Keras
* Imutils
* CV2 (or OpenCV)
* Numpy
* Tensorflow

<a id="p3"></a> 
# Usage:


The program will create a window to display the scene capture by web camera with a label above the detected face specifying the detected emotion with highest probability. 
This particular system uses the pre-trained model provided by Omar, but if you would like to train the data yourself, please refer to his git repository for information on how to do so. 

To run the program, open terminal/console and navigate to the base directory:
```
cd ~/emotion-detection 
```

Then type:
``` 
python hack5.py emotion_count duration_of_emotion
```
where `emotion_count` is an integer and `duration_of_emotion` is a decimal. `duration_of_emotion` must be specified in seconds. The following example will detect 3 emotions with the average of each taken for a duration of 1 second:
```
python hack5.py 3 1
```

The system will measure all emotions detected during the `duration_of_emotion` time period, it will then calculate the most common during this time and add it to the emotions array. It will do this `emotion_count` number of times. The items in the array are then hashed individually and appended to a temporary string (along with the `emotion_count` and `duration_of_emotion` parameters), and the temporary string is then hashed again. This double-hashed string is then returned via terminal for use by the user.




### Dataset:

This project uses [this](https://www.kaggle.com/c/3364/download-all) dataset. For more information on how to use this dataset for training, see [Omar's Repository](https://github.com/omar178/Emotion-recognition)

<a id="p4"></a> 
# Acknowledgements
This work is inspired by [this project](https://github.com/omar178/Emotion-recognition), which was  inspired from [this](https://github.com/oarriaga/face_classification) work and the resources of Adrian Rosebrock. 

Work on turning emotions into a password was a joint effort between [Luke Peacock](https://github.com/LukePeacock) and [Syed Hafizur Reza](https://github.com/sreza1) for the [Hack Sheffield 5 event](https://hacksheffield.co/)

