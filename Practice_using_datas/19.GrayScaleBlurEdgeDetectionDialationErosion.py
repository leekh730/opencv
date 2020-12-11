from cv2 import cv2 as cv

img = cv.imread("datas/images/lena.png")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale Image", imgGray)

imgBlur = cv.GaussianBlur(imgGray, (7, 7), 0)
cv.imshow("Blur Image", imgBlur)
cv.waitKey(0)