import cv2 as opencv
import resize

ir_image = opencv.imread(r'./images/ID-foil-1.bmp', opencv.IMREAD_GRAYSCALE)
vd_image = opencv.imread(r'./images/VD-foil-1.bmp', opencv.COLOR_BGR2GRAY)

# h_ir, w_ir = ir_image.shape[:2]
# h_vd, w_vd = vd_image.shape[:2]
# res_img_linear = opencv.resize(ir_image, (w_vd, h_vd), opencv.INTER_LINEAR)

new_IR = resize.resize_IR_image()
opencv.imshow('START', new_IR)
# opencv.imshow('START', vd_image)


opencv.waitKey(0)
opencv.destroyAllWindows()
