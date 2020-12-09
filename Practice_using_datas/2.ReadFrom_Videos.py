# reference https://docs.opencv.org/4.4.0/d8/dfe/classcv_1_1VideoCapture.html#ac4107fb146a762454a8a87715d9b7c96
import cv2 as cv

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture("./datas/videos/Armbot.mp4")

while True:
    success, img = cap.read()
    img = cv.resize(src = img, dsize=(frameWidth, frameHeight)) # 속도를 빠르게 하기 위해 무조건 resize를 한다
    cv.imshow("Result", img)

    if cv.waitKey(1) == ord('q'): # 'q'를 누르지 않아도 img가 에러가 나면서 밖으로 빠져나가지는 이유는 img가 Armbot.mp4라는 video라서 그렇다.
        break                     # video는 시작과 끝이 있다. 즉, 30초짜리 영상이면 30초 뒤에는 영상이 끝이나므로 더 이상 읽을 img가 없기때문에
                                  # 'q'를 누르지 않아도 img에 none 값을 반환하며 에러를 나타내며 실행이 종료된다.

cap.release()