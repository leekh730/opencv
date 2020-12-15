from cv2 import cv2 as cv
import numpy as np

drawing = False # true if mouse is pressed
ix, iy = -1, -1

def draw_shape(event, x, y, flags, param): # mouse callback func
    global ix, iy, drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0)
    
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2) # if thickness -1 = fill
        cv.imshow("Image", img)

img = np.zeros((512, 512, 3), np.uint8)


while True:
    cv.namedWindow("Image", cv.WINDOW_NORMAL)
    cv.imshow("Image", img)
    cv.setMouseCallback("Image", draw_shape)
    cv.waitKey(0)
    cv.destroyAllWindows()
