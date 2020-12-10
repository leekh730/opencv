import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# final_img = np.hstack((img[:,:,::-1],img[:,:,::-1])) # 한 개의 window에 두 화면을 동시에 띄워줌
# plt.figure()
# plt.imshow(final_img[:,:,::-1])

img = cv.imread("datas/images/lambo.png") # 이미지 파일을 read
plt.figure() # figure는 틀을 만든다고 생각하고
plt.imshow(img[:,:,::-1]) # imshow는 figure로 만든 틀에 imshow로 이미지를 뿌려주고
                          # plt.show()로 우리가 볼 수 있는 window창으로 위 과정을 거쳐 보여준다.
# cv.imshow("Image", img)
print(img.shape)
print(type(img))

imgResize = cv.resize(img, (1000,500)) # resize(입력이미지(src), 출력이미지(dst))
plt.figure()
plt.imshow(imgResize[:,:,::-1])
# cv.imshow("Image Resize", imgResize)
print(imgResize.shape)

imgCropped = img[46:219, 152:495] # img[y,x] = 46:219 slice / 152:495 slice
                                  # 풀어 쓰면, (46,152), (46,495), (219,152), (219,495)[좌상단, 좌하단, 우상단, 우하단]을 점으로 표시
plt.figure()
plt.imshow(imgCropped[:,:,::-1]) #pyplot은 BGR형식이고 cv는 RGB순이여서 -1을 해야 정상적으로 나온다.
# cv.imshow("Image Cropped", imgCropped)

imgCropped2 = img[68:393,62:497] # 쉽게 (68,62), (393,497)로 좌상단과 우하단에 있는 점을 기준으로 해당 좌표 안에 있는 모든 좌표가 해당됨
plt.figure()
plt.imshow(imgCropped2[:,:,::-1])

# ------------------------------------------ practice 1 -------------------------------------------------------
img_p = cv.imread("datas/images/lena.png") # 이미지 파일을 read
plt.figure()
plt.imshow(img_p[:,:,::-1])
imgCropped3 = img_p[40:388,75:394] # 쉽게 (68,62), (393,497)로 좌상단과 우하단에 있는 점을 기준으로 해당 좌표 안에 있는 모든 좌표가 해당됨
plt.figure()
plt.imshow(imgCropped3[:,:,::-1])

# cv.waitKey(3000)
plt.show()