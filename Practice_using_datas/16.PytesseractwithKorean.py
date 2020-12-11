from cv2 import cv2 as cv
from pytesseract import Output
import pytesseract

# img = cv.imread('datas/images/namecard_01.jpg')
# img = cv.imread('datas/images/koreanreceipt.png')
img = cv.imread('datas/images/englishreceipt.png')
# img = cv.imread('datas/images/engrgbreceipt.png')

# threshold add
def thresholding(image):
    return cv.threshold(image, 50, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1] # threshold의 기준을 50으로 잡고, 50보다 크면 255로 나타내고, 작으면 0으로 표현해라는 뜻

custom_config = r'--oem 3 --psm 6 -l kor+kor_vert+eng'
words_string = pytesseract.image_to_string(img)
words = pytesseract.image_to_data(img, config=custom_config, output_type=Output.DICT)
print(words.keys())

n_boxes = len(words['text'])
for i in range(n_boxes):
    if int(words['conf'][i]) > 50:
        (x, y, w, h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

img = cv.resize(img,(860,720))
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = thresholding(img_gray)

cv.imshow("Resource", img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()

elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('datas/images/1.result.png',img)
    cv.destroyAllWindows()

