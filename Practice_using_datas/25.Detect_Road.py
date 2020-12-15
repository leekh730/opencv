from cv2 import cv2 as cv
import numpy as np

cap = cv.VideoCapture("datas/videos/roadway_01.mp4")


while cap.isOpened():
    _, frame = cap.read()
    video_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    
    blur = cv.GaussianBlur(video_gray, (5, 5), 0)
    canny = cv.Canny(blur, 50,100)
    canny_crop = canny[464:703,273:1102]
    video_gray[464:703,273:1102] = canny_crop

    contours, _ = cv.findContours(video_gray, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        epsilon = 0.01 * cv.arcLength(contour, True) # try 0.1
        approx = cv.approxPolyDP(contour, epsilon, True)
        cv.drawContours(frame, [approx], 0, (255, 0, 0), 2) # drawContours(img, contours, index of contours, color, thickness)

    cv.namedWindow("Result", cv.WINDOW_NORMAL) # namedWindow(윈도우 타이틀, 윈도우 사이즈 플래그), default는 autosize
    cv.imshow("Result", frame) # namedWindow에서 지정한 윈도우 타이틀과 같아야함!
    cv.waitKey(1000)

cap.release()

'''
Following Steps:
1. Read and Decode video file into frames
2. Grayscale Conversion of image
3. Reduce noise => GaussianBlur
4. Detecting Edges
5. Mask the canny image
6. Find coordinates of road lanes
7. Fit the coordinates into the canny image
8. Edge detection is done
'''
