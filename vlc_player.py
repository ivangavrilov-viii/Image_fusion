import cv2 as cv
import numpy as np

visual_video = cv.VideoCapture("rtsp://admin:Qwerty404@192.168.1.40:554/Streaming/Channels/101")
ir_video = cv.VideoCapture("rtsp://admin:Qwerty404@192.168.1.40:554/Streaming/Channels/201")

while True:
    ret_visual, frame_visual = visual_video.read()
    ret_ir, frame_ir = ir_video.read()

    # print(frame_visual)

    h = len(frame_visual)
    width = len(frame_visual[0])
    # print(f'Width = {width}')
    # print(f'Height = {h}')

    visual_image = list()

    for i in range(h):
        # print(frame_visual[i])
        # print(len(frame_visual[i]))
        w_list = list()
        for w_elem in frame_visual[i]:
            # print(type(w_elem))
            w_list.append(w_elem)
        w_list = np.array(w_list)
        visual_image.append(w_list)


    print(frame_visual[100][100], visual_image[100][100])


    #     # for j in range(len(frame_visual[1])):
        #     print(f'Element i={i}, j={j}')
        #     print(frame_visual[i][j][0])
        #     # frame_visual[i][j] = np.uint8(frame_visual[i][j])
        #     print(frame_visual[i][j])
    # print(len(frame[0]), len(frame[1]))
    # cv.imshow('VIDEO_VD', visual_image)
    # cv.imshow('VIDEO_IR', frame_ir)
    # cv.waitKey(1)
