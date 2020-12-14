from cv2 import cv2 as cv
import numpy as np
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

# --------------------------------- example 1 ---------------------------------------------------------
# img = cv.imread("datas/images/namecard_01.jpg", cv.IMREAD_GRAYSCALE)
# re_img = cv.resize(img, None, fx=0.5, fy=0.5)
# # cv.imshow("Show img",re_img)
# # cv.waitKey(0)

# try:
#     pts1 = np.float32([[200,232], [467,272], [48,589],[481,664]])
#     pts2 = np.float32([[0,0], [600,0], [0,800],[600,800]])

#     matrix = cv.getPerspectiveTransform(pts1, pts2)

#     result = cv.warpPerspective(re_img, matrix, (600,800))

#     # ret,thresh1 = cv.threshold(result, 150, 255, cv.THRESH_BINARY) # 150 < pixel = 0
#     # ret,thresh2 = cv.threshold(result, 150, 255, cv.THRESH_BINARY_INV) # 150 > pixel = 0
#     # ret,thresh3 = cv.threshold(result, 150, 255, cv.THRESH_TRUNC) # 150 < pixel = pixel
#     # ret,thresh4 = cv.threshold(result, 150, 255, cv.THRESH_TOZERO) # 150 > pixel = pixel
#     # ret,thresh5 = cv.threshold(result, 150, 255, cv.THRESH_TOZERO_INV) # 150 < pixel = 0

#     # titles = ["Original Image", "Binary", "Binary_Inv", "Trunc", "Tozero", "Tozero_Inv"]
#     # images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

#     # for i in range(6):
#     #     plt.subplot(2, 3, i + 1)
#     #     plt.imshow(images[i], 'gray', vmin=0, vmax=255)
#     #     plt.title(titles[i])
#     #     plt.xticks([])
#     #     plt.yticks([])

#     # plt.show()

#     threshold = cv.threshold(result, 150, 255, cv.THRESH_BINARY)

#     read_text = r'--oem 3 --psm 6 -l eng'
#     words_string = pytesseract.image_to_string(result)
#     words = pytesseract.image_to_data(result, config=read_text, output_type=Output.DICT)
#     print(words.keys())

#     n_boxes = len(words['text'])
#     for i in range(n_boxes):
#         if int(words['conf'][i]) > 10:
#             (x, y, w, h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
#             img = cv.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 1)

# except:
#     print("Find Error")

# finally:
#     cv.imshow("Result", result)
#     cv.waitKey(0)
#     if cv.waitKey(1) == 27:
#         cv.destroyAllWindows()
# ------------------- example 2----------------------------------------------------------------------
img2 = cv.imread("datas/images/past_carnum.png")

img2crop = img2[244:290,94:160] # y좌표, x 좌표 순, 그 이유는 np는 y,x좌표 순으로 진행되며, opencv는 x,y순으로 진행된다.
                                # np라는 것을 알 수 있는 것은 슬라이싱을 했기 때문에 np라는 것을 알 수 있다.
img2resize = cv.resize(img2crop, None, fx=4, fy=4)
cv.imshow("Image",img2resize)
cv.waitKey(0)

