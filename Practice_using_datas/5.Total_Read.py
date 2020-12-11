# Read image, Videos, Webcam

import cvfrom cv2 import cv2 as cv

frameWidth = 640
frameHeight = 480

# img = cv.imread('./datas/images/lena.png')
# video = cv.VideoCapture("./datas/videos/Armbot.mp4")
# webcam = cv.VideoCapture(2)
mul = cv.VideoCapture("./datas/videos/Armbot.mp4")
# webcam.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)         
# webcam.set(4,frameHeight)

try:
    # cv.imshow('Lena Soderberg', img)
    # cv.waitKey(0)
    # if cv.waitKey(0) == 105: # ASCII Code 105는 'i'
    #     cv.destroyWindow()

    while True:
        success, vid = mul.read()
        vid = cv.resize(src = vid, dsize=(frameWidth, frameHeight)) 
        cv.imshow("Play Video", vid)
        if cv.waitKey(5000) == ord('v'): # ord는 키보드로 치는 문자를 ASCII code로 반환, 즉 v = 118
            break               

    while mul.isOpened():
        success, web = mul.read()
        cv.imshow("Display mul",web)
        if cv.waitKey(1) == ord('w'):
            break

except:
    pass

finally:
    mul.release()
    # webcam.release()
    if cv.waitKey(1) == 27: # 27는 'ESC'
        cv.destroyAllWindows()
