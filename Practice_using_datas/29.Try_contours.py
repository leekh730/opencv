from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/shapes.png")
cv.imshow("Source", img)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU) # threshold(img(input array), threshold value, maxvalue, type)

try:
    contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        print(x, y, w, h)
        epsilon = 0.01 * cv.arcLength(contour, True) # try 0.1
        approx = cv.approxPolyDP(contour, epsilon, True)
        print(len(approx))
        cv.drawContours(img, [approx], 0, (255, 0, 0), 2) # drawContours(img, contours, index of contours, color, thickness)
        
        if len(approx) == 3:
            cv.putText(img, "Tri", (x - 10, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, 0, 1)
        elif len(approx) == 4:
            cv.putText(img, "Squ", (x - 10, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, 0, 1)
        else:
            cv.putText(img, "Cir", (x - 10, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, 0, 1)

        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
except:
    print("Find Error")

finally:
    while True:
        cv.imshow("Result",img)
        if cv.waitKey(1) == 27:
            break
