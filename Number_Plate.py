import cv2
import os
from datetime import datetime
import textext
global count
# def rename(scount, ecount):
def rename(count,t):
 cfp = r'Saved_Plates\count.txt'
 if os.path.exists(cfp): 
    with open(cfp, 'r') as file:
            count = int(file.read())

 original_name = rf'Saved_Plates\p{count}.jpg'
 renamed_to = rf'Saved_Plates\p{count}_{t}.jpg'  
 if os.path.exists(original_name):
  os.rename(original_name, renamed_to)
 print(f"File {original_name} successfully renamed to {renamed_to}")
 return renamed_to
def load_count():
    cfp = r'Saved_Plates\count.txt'
    if os.path.exists(cfp):
        with open(cfp, 'r') as file:
            count = int(file.read())
    else:
        count = 0
    return count 
def save_count(count):
    cfp = r'Saved_Plates\count.txt'
    with open(cfp, 'w') as file:
        file.write(str(count))
def project():
    timenow = datetime.now()
    t = timenow.strftime('%d-%m-%Y %H-%M-%S')
    print(t)
    platecascade = cv2.CascadeClassifier(r'haarcascade_russian_plate_number.xml')
    minarea = 500
    count = load_count()
    scount = count
    cam = cv2.VideoCapture(0)
    # address='https://192.168.137.183:8080/video'
    # cam.open(address)
    while True:
        success, img = cam.read()
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        nplates = platecascade.detectMultiScale(grayscale, 1.1, 4)
        for x, y, w, h in nplates:
            area = w * h
            if area > minarea:
                cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
                cv2.putText(img, 'NumberPlate', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225), 2)
                reqimg = img[y:y+h, x:x+w]
                cv2.imshow('Plate', reqimg)
        cv2.imshow('NPDS', img)
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:
            ecount = count
            break
        if key == ord('s'):
            timenow = datetime.now()
            t = timenow.strftime('%d-%m-%Y %H-%M-%S')
            cv2.imwrite(r'Saved_Plates\p' + str(count) + '.jpg', reqimg)
            cv2.putText(img, 'SAVED', (15, 265), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 225, 225), 2)
            rn=rename(count,t)
            textext.textext(rn)
            count += 1
            save_count(count)
    cam.release()
    cv2.destroyAllWindows()
    # rename(scount, ecount)
if __name__ == '__main__':
    project()
