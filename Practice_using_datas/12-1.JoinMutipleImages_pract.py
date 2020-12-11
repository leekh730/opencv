import cv2 as cv
import numpy as np

# image 불러오기
img = cv.imread("datas/images/lena.png")
# cv.imshow("Image", img) # 이미지가 잘 불러와지는지 확인만 하고 주석처리
# print(img.shape)

# camera 불러오기
camera = cv.VideoCapture(0) # web cam device0번 사용
# cam_wid = camera.get(cv.CAP_PROP_FRAME_WIDTH) # 카메라 width 사이즈 확인
# cam_hei = camera.get(cv.CAP_PROP_FRAME_HEIGHT) # 카메라 height 사이즈 확인
# print(cam_wid) # float임으로 int로 변경 필요
# print(cam_hei)

# camera size resize하기
wid = 640
hei = 480
cam_resize_wid = camera.set(cv.CAP_PROP_FRAME_WIDTH, wid)
cam_resize_hei = camera.set(cv.CAP_PROP_FRAME_HEIGHT, hei)
# print(camera.shape) # 에러 출력, 이유는 camera는 array가 아니라 하나의 class 객체이기 때문에 shape가 찍히지 않는다.
# print(type(camera))

# image resize 하기 (기준은 카메라 resize한 것을 기준으로)
img_resize = cv.resize(img, (wid, hei))
# print(img_resize.shape)

# video 불러오기
video = cv.VideoCapture("datas/videos/output.avi")
# vid_wid = video.get(cv.CAP_PROP_FRAME_WIDTH)
# vid_hei = video.get(cv.CAP_PROP_FRAME_HEIGHT)
# print(vid_wid, vid_hei)

# camera2 불러오기
camera2 = cv.VideoCapture(2) # web cam device2번 사용
# cam2_wid = camera2.get(cv.CAP_PROP_FRAME_WIDTH) # 카메라 width 사이즈 확인
# cam2_hei = camera2.get(cv.CAP_PROP_FRAME_HEIGHT) # 카메라 height 사이즈 확인
# print(cam2_wid, cam2_hei) # float임으로 int로 변경 필요

while camera.isOpened() and camera2.isOpened():
    success, cam = camera.read()
    success, vid = video.read()
    success, cam2 = camera2.read()
    # h,w,c = cam.shape # h = 480, w = 640, c = 3
    # h,w,c = cam2.shape # h = 240, w = 640, c = 3

    #cam2의 h=240으로 cam1의 기준을 맞추기 위해 cam2를 두 개 붙여준다. => h = 480, w = 640, c = 3
    mer_cam2 = np.vstack((cam2, cam2))

    mer_img_cam = np.hstack((img_resize, cam)) # resize한 img와 cam을 horizontal로 연결
    mer_vid_cam2 = np.hstack((vid,mer_cam2)) # video와 cam2를 merge한 것을 horizontal로 연결

    mer_hstacks = np.vstack((mer_img_cam, mer_vid_cam2)) # vertical로 위 두개를 연결

    cv.imshow("Result", mer_hstacks)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
video.release()
camera2.release()