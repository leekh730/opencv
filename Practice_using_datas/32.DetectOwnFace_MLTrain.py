from cv2 import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join

directory_name = "datas/images/faces/"
onlyfiles = [f for f in listdir(directory_name) if isfile(join(directory_name,f))]

Training_Data, Labels = list(), list() # training_data는 train시키고자 하는 데이터, labels는 정답 값

for i, files in enumerate(onlyfiles):
    image_path = directory_name + onlyfiles[i]
    images = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype = np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype = np.int32)
model = cv.face.LBPHFaceRecognizer_create() # pip install opencv-contrib-python, LBPHFaceRecognizer를 실행하기 위해서 확장팩을 설치
print("Model Training Start!!!!!")
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model Training Complete!!!!!")
model.save('save.yml')

