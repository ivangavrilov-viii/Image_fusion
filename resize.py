import cv2 as opencv


def resize_IR_image():
    ir_image = opencv.imread(r'./images/ID-foil-1.bmp', opencv.IMREAD_GRAYSCALE)
    res_img_linear = opencv.resize(ir_image, (1920, 1080), opencv.INTER_LINEAR)
    return res_img_linear
