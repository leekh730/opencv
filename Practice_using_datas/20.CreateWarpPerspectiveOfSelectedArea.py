from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/cards.jpg")
try:
    cv.imshow("Image", img)

    width, height = 250, 350

    pts1 = np.float32([[111, 219], [287,188], [154,482], [352,440]]) # 좌상단, 우상단, 좌하단, 우하단
    pts2 = np.float32([[0, 0], [width,0], [0,height], [width,height]]) # 좌상단, 우상단, 좌하단, 우하단

    matrix = cv.getPerspectiveTransform(pts1, pts2)

    imgOutput = cv.warpPerspective(img, matrix, (width, height))

    cv.imshow("Output", imgOutput)

except:
    print("Something is Wrong, Please find ERROR")

finally:
    while True:
        if cv.waitKey(1) == 27:
            break