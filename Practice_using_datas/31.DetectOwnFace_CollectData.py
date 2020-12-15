import os
from cv2 import cv2 as cv

try:
    directory_name = "./datas/images/faces/"
    os.makedirs(directory_name, exist_ok= True)
    print("Directory {} created Successfully".format(directory_name))

except OSError as error:
    print("Directory {} can not be created".format(directory_name))

cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)
count = 0

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cropped_face = gray[y:y+h,x:x+w]
    
    cropped_area = gray
    put_text = ' '

    if cropped_area is not None:
        count += 1
        area = cv.resize(cropped_area, (200, 200))

        file_name = directory_name + "user" + str(count) + ".jpg"
        cv.imwrite(file_name, area)
        put_text = "Face Found!, imwrite() count" + str(count)
    
    else:
        put_text = "Face not Found!"

    
    area = cv.resize(cropped_area, (640, 480))
    cv.putText(area, put_text, (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    
    cv.imshow("Camera", frame)
    cv.imshow("Face Cropper", area)

    if cv.waitKey(1) == ord('q') or count == 100:
        break

cap.release()
