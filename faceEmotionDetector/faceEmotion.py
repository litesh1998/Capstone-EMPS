import numpy as np
import cv2
import tensorflow as tf
import json
import time
import os
from colorama import Fore

cwd = os.path.abspath("../")
comModel = os.path.join(cwd, "faceEmotionDetector","comModel.h5")
pols = os.path.join(cwd, "faceEmotionDetector","pols.json")
haarcascade = os.path.join(cwd, "faceEmotionDetector","haarcascade_frontalface_default.xml")



dic = {}
# with open("faceEmotionDetector\pols.json") as file:
with open(pols) as file:
    try:
        dic = json.load(file)
    except:
        print("json file empty")
if dic == False:
    dic = {"Angry": 0, "Disgusted": 0, "Fearful": 0, "Happy": 0,
           "Neutral": 0, "Sad": 0, "Surprised": 0, "time": time.time()}


def faceEmotion():
    # model = tf.keras.models.load_model("faceEmotionDetector\comModel.h5")
    model = tf.keras.models.load_model(comModel)
    cv2.ocl.setUseOpenCL(False)
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful",
                    3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    cap = cv2.VideoCapture(0)
    t = time.time()
    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        if not ret:
            return
        # facecasc = cv2.CascadeClassifier('faceEmotionDetector\haarcascade_frontalface_default.xml')
        facecasc = cv2.CascadeClassifier(haarcascade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(
                cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            emotion = emotion_dict[maxindex]
            # yield emotion
            global dic
            if time.time()-dic["time"] >= 10:
                dic = {"Angry": 0, "Disgusted": 0, "Fearful": 0, "Happy": 0,
                       "Neutral": 0, "Sad": 0, "Surprised": 0, "time": time.time()}
                print(Fore.MAGENTA + "restartin polls" + Fore.RESET)
            dic[emotion] += 1
            dic["time"] = time.time()
            # with open("faceEmotionDetector\pols.json", "w") as file:
            with open(pols, "w") as file:
                json.dump(dic, file)
            print(Fore.BLUE + emotion + Fore.RESET, end = " | ")
            cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time()-t > 10:
            break
    print("\n")
    cap.release()
    cv2.destroyAllWindows()

def returnEmotion():
    # with open("faceEmotionDetector\pols.json") as file:
    with open(pols) as file:
        dic = json.load(file)
        emDic={}
        for key,value in dic.items():
            if key != "time":
                emDic[key]=value
        maxEmotion = max(emDic, key= lambda x: emDic[x]) 
        print(Fore.GREEN + "Final Detected Emotion:\t" + Fore.RESET + Fore.CYAN + maxEmotion + Fore.RESET)
        return maxEmotion
        



if __name__ == "__main__":
    faceEmotion()
    # returnEmotion()
