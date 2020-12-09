# reference https://docs.opencv.org/4.2.0/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
import os
import cv2 as cv
print(os.getcwd()) # /home/rapa/Documents/opencv

img = cv.imread("./datas/images/lena.png")

cv.imshow("Lena Soderberg",img)
cv.waitKey(0) # waiteKey가 0이면 화면이 멈추고
# cv.waitKey(5000) # waitKey는 milliseconds를 기본 단위를 사용하여 1000을 입력하면 1초
