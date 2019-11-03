from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
from statistics import mode
# parameters for loading data and images
detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'

# hyper-parameters for bounding boxes shape
# loading models
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
 "neutral"]

#feelings_faces = []
#for index, emotion in enumerate(EMOTIONS):
   # feelings_faces.append(cv2.imread('emojis/' + emotion + '.png', -1))

def start_stream(max_emotionx,timex):
    #counter and ticks are same thing here
    counter = 0
    emo_array=[]
    emo_pass_arr = []
    #estimated that each loop is around 1.04/30 seconds
    one_tick_in_seconds = 1.04/30
    sec_to_tick = timex/one_tick_in_seconds
    #convert seconds to ticks
    max_count = round(sec_to_tick)
    max_emotion = max_emotionx
    stream_finish = False
    # starting video streaming
    cv2.namedWindow('your_face')
    camera = cv2.VideoCapture(0)
    while True:
        frame = camera.read()[1]
        #reading the frame
        frame = imutils.resize(frame,width=300)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
        
        frameClone = frame.copy()
        if len(faces) > 0:
            faces = sorted(faces, reverse=True,
            key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces
            # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
            # the ROI for classification via the CNN
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            
            
            preds = emotion_classifier.predict(roi)[0]
            label = EMOTIONS[preds.argmax()]
            if counter != max_count:
                counter=counter+1
                emo_array.append(label)
            elif counter == max_count:
                #picks most common emotion found for given time interval
                emo_pass_arr.append(mode(emo_array))
                counter = 0
                emo_array = []
        else: continue
        for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
            cv2.putText(frameClone, label, (fX, fY - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        cv2.imshow('your_face', frameClone)

        #if the stream has recorded the maximum number of emotions needed to be recorded, it ends the stream
        if len(emo_pass_arr) == max_emotion:
            stream_finish = True
        
        if cv2.waitKey(1) & stream_finish:
            break

    camera.release()
    cv2.destroyAllWindows()
    #returns array of emotions
    return emo_pass_arr