import numpy as np
import matplotlib.pyplot as plt

arr_img = np.zeros((150,200,3), np.uint8)
red_img = arr_img.copy()
green_img = arr_img.copy()
blue_img = arr_img.copy()

red_img[:,:,0] = 255    #red
green_img[:,:,1] = 255  #green
blue_img[:,:,2] = 255   #blue


fig1 = plt.figure(1) # figure는 window창을 띄워주는 명령어
plt.imshow(red_img) # imshow는 imageshow로 띄워진 window창에 결과값을 뿌려주는 명령어

fig2 = plt.figure(2)
plt.imshow(blue_img)

fig3 = plt.figure(3)
plt.imshow(green_img)

plt.show() # show를 해야 창을 띄워줌