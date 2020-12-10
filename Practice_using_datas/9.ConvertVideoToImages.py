import os
import cv2 as cv

directoryname = os.getcwd() + '/datas/images/Imageframes/'
files = os.listdir(directoryname)
filename = directoryname + '/image_0.png'

img = cv.imread(filename)
height, width, layers = img.shape
size = (width, height)
fps = 15

filename_output = directoryname + 'output_video.avi'
out_avi = cv.VideoWriter(filename_output, cv.VideoWriter_fourcc(*'DIVX'), fps, size) # fourcc is codec

for count in range(len(files)):
    filename = directoryname + "/image_" + str(count) + ".png"
    img = cv.imread(filename)

    if img is not None:
        cv.imshow('image_' + str(count), img)
        out_avi.write(img)
        cv.waitKey(1)

out_avi.release()
cv.waitKey(5000)
cv.destroyAllWindows()

