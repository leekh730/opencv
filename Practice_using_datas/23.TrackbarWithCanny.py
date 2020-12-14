from cv2 import cv2 as cv

def nothing():
    pass

cv.namedWindow("Canny Edge")
cv.createTrackbar("Low Threshold", "Canny Edge", 0, 1000, nothing)
cv.createTrackbar("High Threshold", "Canny Edge", 1000, 1500, nothing)

img_gray = cv.imread("datas/images/shapes_canny.png", cv.IMREAD_GRAYSCALE)

while True:
    low = cv.getTrackbarPos("Low Threshold", "Canny Edge")
    high = cv.getTrackbarPos("High Threshold", "Canny Edge")
    img_canny = cv.Canny(img_gray, low, high)
    cv.imshow("Canny Edge", img_canny)

    if cv.waitKey(1) == ord('q'):
        break

