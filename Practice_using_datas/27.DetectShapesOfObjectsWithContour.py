from cv2 import cv2 as cv

img_color = cv.imread("datas/images/shapes.png")
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret,img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # findContours(img, mode, method)
                                                                                # https://docs.opencv.org/4.4.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0

for contour in contours:
    area = cv.contourArea(contour)
    cv.drawContours(img_color, [contour], 0, (255, 0, 0), 1) # contours가 list형태로 되어있어, 형변환 없이 contour도 list타입으로 받기 위해 []를 씌워줌

cv.imshow("Result", img_color)
cv.waitKey(0)

'''
What is contours?
A curve joining all the continuous points, havinig same color or intensity(강도,세기).
Contours are a useful tool for Shape Analysis and Object Detection and Recognition

1. better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
2. FindContours function modifies the source images.
3. Findig contours is like finding white object from black background. So, object to be found should be white and background should be black.

Reference : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started
'''
