from cv2 import cv2 as cv

img_color_approx = cv.imread("datas/images/shapes.png")
img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY)
ret,img_binary = cv.threshold(img_gray, 127, 255, 0)

# contour(윤곽)
contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # findContours(img, contour retrieval mode(algoruthm), contour approxiation method)

for contour in contours:
    x, y, w, h = cv.boundingRect(contour)
    print(x, y, w, h)
    epsilon = 0.02 * cv.arcLength(contour, True) # try 0.1
    approx = cv.approxPolyDP(contour, epsilon, True)
    print(len(approx))
    cv.drawContours(img_color_approx, [approx], 0, (0, 255, 255), 3) # drawContours(img, contours, index of contours, color, thickness)

cv.imshow("Result", img_color_approx)
cv.waitKey(0)