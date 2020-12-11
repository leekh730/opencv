# try, except 문 사용해보기
# tyy, excpet문은 내가 예상했던 에러들이 아닌 그 외의 에러들을 캐치하기 위해 사용한다.

from cv2 import cv2 as cv

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(2)

try:
    while(cap.isOpened()):
        results, frame = cap.read()
        cv.imshow('Display Result', frame)
        if cv.waitKey(1) == 27: # ASCII code로 숫자 27은 키보드의 'ESC'를 의미, 즉, "ESC"를 누르면 waitKey(1)(0.001초)멈추었다가 break문을 통해 나가짐
            break

except:
    pass

finally:
    cap.release() # when everything done, release the capture
    cv.destroyAllWindows() # 요즘은 버전이 업그레이드 되면서 잘 사용하지는 않는다.