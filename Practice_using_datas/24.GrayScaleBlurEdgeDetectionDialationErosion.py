from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/lena.png")
imgCanny = cv.Canny(img, 10, 300) # Canny(img, 4단계에서의 최소값, 4단계에서의 최대값)
cv.imshow("Canny Image", imgCanny)

kernel = np.ones((3,3), np.uint8)
imgDialation = cv.dilate(imgCanny, kernel, iterations=1) # dilate(img, dilate를 위한 커널, 반복 횟수)
cv.imshow("Dilation Image", imgDialation)

imgEroded = cv.erode(imgDialation, kernel, iterations=1)
cv.imshow("Eroded Image", imgEroded)

cv.waitKey(0)
cv.destroyAllWindows()

'''
canny description = https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

커널은 Image Transformation을 결정하는 구조화된 요소

Erosion은 이미지를 침식시키는 것으로, Foreground가 되는 이미지의 경계부분을 침식시켜 Background 이미지로 전환된다.
즉, 흐릿한 경계부분은 배경으로 만들어 버림

Dilation은 이미지를 팽창시키는것으로 Erosion의 반대
'''