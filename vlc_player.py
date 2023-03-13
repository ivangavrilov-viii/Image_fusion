import cv2 as cv
import numpy as np

visual_video = cv.VideoCapture("rtsp://admin:Qwerty404@192.168.1.40:554/Streaming/Channels/101")
ir_video = cv.VideoCapture("rtsp://admin:Qwerty404@192.168.1.40:554/Streaming/Channels/201")

while True:
    ret_visual, frame_visual = visual_video.read()
    ret_ir, frame_ir = ir_video.read()

    for i in range(len(frame_visual[0])):
        print(i)
        for j in range(len(frame_visual[1])):
            print(f'Element i={i}, j={j}')
            print(frame_visual[i][j][0])
            frame_visual[i][j] = np.uint8(frame_visual[i][j])
            print(frame_visual[i][j])
    # print(len(frame[0]), len(frame[1])s)
    cv.imshow('VIDEO_VD', frame_visual)
    cv.imshow('VIDEO_IR', frame_ir)
    cv.waitKey(1)