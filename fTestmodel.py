import cv2
import os
import fDataCollect
import openpyxl
from datetime import datetime

tn=datetime.now()
t=tn.strftime('%H:%M:%S')
d=tn.strftime('%d-%m-%Y')

name=fDataCollect.name
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(r'D:\DRP Project\haarcascade_frontalface_default.xml')
no=fDataCollect.id
no=int(no)
c=1
c=int(c)
recognizer = cv2.face.LBPHFaceRecognizer.create()
recognizer.read('trainer.yml')
name_list=['']*100
name_list.insert(no,fDataCollect.name)
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        serialno,conf=recognizer.predict(gray[y:y+h, x:x+w])
        if conf<70:
           cv2.putText(frame,name_list[serialno],(x,y-40),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,225),2)
           cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        else:
           cv2.putText(frame,'',(x,y-40),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,225),2)
           cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)            
    cv2.imshow('Face', frame)
    k = cv2.waitKey(1)
    if k==27 or k=='q':  
            break

cv2.destroyAllWindows()