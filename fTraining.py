
import cv2 
import numpy as np
from PIL import Image
import os
import fDataCollect as fdc

recognizer = cv2.face.LBPHFaceRecognizer.create()
id = fdc.id
id=int(id)

path='datasets/user{}'.format(id)

def getImageID(path):
    imagepath=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for imagepaths in imagepath:
        faceimage=Image.open(imagepaths).convert('L')
        faceNP=np.array(faceimage,'uint8')
        faces.append(faceNP)
        ids.append(id)
        cv2.imshow('Training...', faceNP)
        cv2.waitKey(1)
    return ids,faces

IDs,facedata=getImageID(path)
recognizer.train(facedata,np.array(IDs))
recognizer.write('trainer.yml')
cv2.destroyAllWindows()
print('Training Completed')