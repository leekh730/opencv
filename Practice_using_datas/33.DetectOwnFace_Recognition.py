from cv2 import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join


cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)
count = 0
model = cv.face.LBPHFaceRecognizer_create()
model.read('save.yml')

while cap.isOpened():
    ret, frame = cap.read()

    try:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cropped_face = gray[y:y+h,x:x+w]
        
        cropped_area = cropped_face
        put_text = ' '

        result = model.predict(cropped_area)
        display_string = ""
        if result[1] < 500:
            confidence = int(100 * (1 - (result[1] / 300)))
            display_string = str(confidence) + "% Confidence, "
        
        if confidence > 75:
            display_string = display_string + "Unlocked"
        
        else:
            display_string = display_string + "Locked"

        cv.putText(frame, display_string, (250,450), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv.imshow("Face Cropper", frame)
    
    except:
        pass

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
