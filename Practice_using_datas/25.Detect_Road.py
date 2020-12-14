from cv2 import cv2 as cv

cap = cv.VideoCapture("datas/videos/roadway_01.mp4")


while cap.isOpened():
    _, frame = cap.read()
    video_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    
    blur = cv.GaussianBlur(video_gray, (5, 5), 0)
    canny = cv.Canny(blur, 50,100)

    canny_crop = canny[278:711,443:1086]

    cv.imshow("Result", canny_crop)
    cv.waitKey(5000)

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
