import cv2
import os

global id
global name
id = input('Enter your ID: ')
name=input('Enter your Name: ')
def training():
    global id
    global name
    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier(r'D:\DRP Project\haarcascade_frontalface_default.xml')

    count = 0
    while True:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
            count += 1
            if not os.path.exists('datasets/user' + id):
                os.mkdir('datasets/user' + id)
            cv2.imwrite('datasets/user{}/user.{}.{}.jpg'.format(id, id, count), gray[y:y+h, x:x+w])

        cv2.imshow('Face', frame)
        k = cv2.waitKey(1)
        if count>100:  
            break

    cv2.destroyAllWindows()
    print('DataSet Collection Done.......')

if __name__=='__main__':
 t=training()
 id=id
 name=name