from cv2 import cv2 as cv
from pytesseract import Output
import pytesseract
import matplotlib.pyplot as plt

img = cv.imread('datas/images/sudoku.jpg', cv.IMREAD_GRAYSCALE)
ret,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 4) # MEAN은 평균, C는 Const, 11은 11x11의 filterwindow(filterwindow는 무조건 홀수여야 함), 
                                                                                        # 2는 가중치라고 하고 filterwindow에서 구해진 평균 값에서 2를 뺀 것
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 4) # 가우시안은 정규분포

titles = ["Original Image", "Binary", "Binary_Inv", "Trunc", "Tozero", "Tozero_Inv"]
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()