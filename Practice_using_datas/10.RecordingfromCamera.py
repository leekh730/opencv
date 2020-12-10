import cv2 as cv

cap = cv.VideoCapture(0) # 연결된 device0을 선택
frameWidth = 640
frameHeight = 480
# fps = 20.0
# (frameWidth, frameHeight) = (640,480) # 위에 정해준 값을 한 줄로 표현

cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
# cap.set(cv.CAP_PROP_FPS, fps)
cap.set(4,frameHeight)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out_avi = cv.VideoWriter('datas/videos/output.avi', fourcc, 20.0, (640,480)) # VideoWriter(filename, fourcc, fps, frameSize[, isColor])
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out_mp4 = cv.VideoWriter('datas/videos/output.mp4', fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    out_avi.write(frame)
    out_mp4.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out_avi.release()
out_mp4.release()
