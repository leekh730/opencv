from cv2 import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
# cap = cv.VideoCapture(0) # 파라미터를 0을 넣으면 ls -al /dev/video*라고 했을때 나오는 리스트에서 video0을 의미
                         # window에서는 해당 USB의 device명이 나오므로 해당 device명을 파라미터로 넣어줘야 함

cap = cv.VideoCapture(2)

cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth) # set이란 unordered and unindexed collection
                                             # CAP_PROP_FRAME_WIDTH의 datatype은 Enumerate
cap.set(4,frameHeight)

while cap.isOpened():
    success, img = cap.read() # while 아래에 success와 img가 있는 것은 python은 return 값을 여러 개를 가질 수 있어서이다.
                              # 즉, 풀어서 쓰면 return success, img = cap.read() 와 같다.
                              # img는 numpy array type으로 되어 있다. success와 img 각각의 return되는 값을 통해 에러 검사를 하는 방법은 아래와 같다.
    cv.imshow("Result",img)
    if cv.waitKey(1) == ord('q'): # cv.waitKey가 키보드 'q'를 눌렀을 때, 대입되어 실행되고 break문으로 나오게 된다.
        break

#----------------------------------------------------------------------------------------------    
    # success와 img 각각의 return되는 값을 통해 에러 검사를 하는 방법
    # if success == False: # img가 없으면 success가 false로 바뀌고 break문을 통해 빠져나온다.
    #     break
    # if isinstance(img, np.ndarray):
    #     cv.imshow("Result", img)
    #     if cv.waitKey(1) == ord('q'): # cv.waitKey가 키보드 'q'를 눌렀을 때, 대입되어 실행되고 break문으로 나오게 된다.
    #         break
    # else:
    #     break
#----------------------------------------------------------------------------------------------        

cap.release()
