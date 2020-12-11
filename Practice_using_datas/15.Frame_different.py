from cv2 import cv2 as cv
import numpy as np

def frame_diff(prev_frame, cur_frame, next_frame):
    diff_frames_1 = cv.absdiff(next_frame, cur_frame) # absdiff(src1, src2), src는 array or scalar, absdiff는 absoulute diffent로 절대값을 비교
    diff_frames_2 = cv.absdiff(cur_frame, prev_frame)
    return_diff = cv.absdiff(diff_frames_1, diff_frames_2)

    threshold = len(return_diff[np.where(return_diff > 2)]) # np.where is return elements chosen from x or y depending on condition
    if threshold > 500:
        print('threshold > 200 : ', threshold)

    return return_diff, diff_frames_1

def get_frame(cap, scaling):
    _, frame = cap.read()
    frame = cv.resize(frame, None, fx = scaling, fy = scaling, interpolation = cv.INTER_AREA)
    # frame = cv.resize(frame, (480,960), interpolation = cv.INTER_AREA)
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    return gray

cap = cv.VideoCapture(0)
scaling = 0.5
prev_frame = get_frame(cap, scaling)
cur_frame = get_frame(cap, scaling)
next_frame = get_frame(cap, scaling)

while True:
    a,b = frame_diff(prev_frame, cur_frame, next_frame)
    img = np.hstack((a,b))
    cv.imshow("Object Movement", img)
    # cv.imshow("Object Movement", frame_diff(prev_frame, cur_frame, next_frame))
    prev_frame = cur_frame
    cur_frame = next_frame
    next_frame = get_frame(cap, scaling)
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()