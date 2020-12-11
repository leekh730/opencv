from cv2 import cv2 as cv
from pytesseract import Output
import pytesseract
import matplotlib.pyplot as plt

# img = cv.imread('datas/images/radial_gradient.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.imread('datas/images/engrgbreceipt.png')
img = cv.imread('datas/images/koreanreceipt.png',cv.IMREAD_GRAYSCALE)

ret,thresh1 = cv.threshold(img, 150, 255, cv.THRESH_BINARY) # 150 < pixel = 0
ret,thresh2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV) # 150 > pixel = 0
ret,thresh3 = cv.threshold(img, 150, 255, cv.THRESH_TRUNC) # 150 < pixel = pixel
ret,thresh4 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO) # 150 > pixel = pixel
ret,thresh5 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO_INV) # 150 < pixel = 0

titles = ["Original Image", "Binary", "Binary_Inv", "Trunc", "Tozero", "Tozero_Inv"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()