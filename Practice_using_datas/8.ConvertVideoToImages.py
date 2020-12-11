import os
from cv2 import cv2 as cv

try:
    directory = "./datas/images/Imageframes"
    os.makedirs(directory, exist_ok= True)
    print("Directory {} created Successfully".format(directory))
except OSError as error:
    print("Directory {} can not be created".format(directory))

def writeFrame(videocapture, second, cnt):
    videocapture.set(cv.CAP_PROP_POS_MSEC, second*1000)
    hasFrames, image = videocapture.read()
    if hasFrames:
        cv.imwrite(directory + "/image_" + str(cnt) + ".png", image)
    return hasFrames


filename = "./datas/videos/Armbot.mp4"
cap = cv.VideoCapture(filename)
sec = 0
count = 0
frameRate = 0.5

success = cap.isOpened()
while success:
    sec = sec + frameRate
    success = writeFrame(cap, sec, count)
    count = count + 1
