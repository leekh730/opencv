from cv2 import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512,512,3), np.uint8)
print(img)

img[:] = 255,0,0 # 위 np.zeros(512,512,3)를 아래와 같이 풀어쓰는 것을 한 줄로 완료
# img[:,:,0] = 255
# img[:,:,1] = 0
# img[:,:,2] = 0
print(img.shape)

cv.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3) # (img.shape[1], img.shape[0])중에서 img.shape[1]는 가로, img.shape[0]는 세로를 의미
cv.rectangle(img, (0,0), (250, 350), (0,0,255), 2)

cv.circle(img, (400,50), 30, (255, 255, 0), 5)
cv.putText(img, "OPENCV", (300, 200), cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

x, y, w, h = 310, 320, 150, 160
cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.putText(img, "Bounding Box", (x - 10, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
