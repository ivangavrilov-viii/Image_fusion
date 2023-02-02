import cv2 as opencv
from methods_of_aggregation import maximum_method, averaging_method, mask_method, \
    power_transformation_method, weight_function_method

from dispersion import dispersion
from correl import correlation_coefficient
from entropia import calcEntropy2dSpeedUp
from time import time

""" Reading two original grayscale images """
vd_image = opencv.imread(r'./images/building_photos/TV.PNG', opencv.IMREAD_GRAYSCALE)
ir_image = opencv.imread(r'./images/building_photos/TIR.PNG', opencv.IMREAD_GRAYSCALE)

# """ Displaying images before fusion """
# opencv.imshow('VD', vd_image)
# opencv.imshow('VIR', ir_image)

""" Get and saving images by various methods of image fusion """
max_method_image = maximum_method(vd_image, ir_image)
opencv.imwrite('./images/fusion_images/maximum_method.png', max_method_image)

average_image = averaging_method(vd_image, ir_image)
opencv.imwrite('./images/fusion_images/averaging_method.png', average_image)

mask_image = mask_method(vd_image, ir_image, 10)
opencv.imwrite('./images/fusion_images/mask_method.png', mask_image)

ptm_image = power_transformation_method(vd_image, ir_image)
opencv.imwrite('./images/fusion_images/power_transformation_method.png', ptm_image)

wfm_image = weight_function_method(vd_image, ir_image)
opencv.imwrite('./images/fusion_images/weight_function_method.png', wfm_image)


""" Image dispersion calculation """
complexed_image = opencv.imread(r'./images/fusion_images/maximum_method.png', opencv.IMREAD_GRAYSCALE)
compared_images = [vd_image, ir_image, complexed_image]
dispersion(compared_images)


""" Correlation coefficient of images calculation """
correl_coef = correlation_coefficient(vd_image, complexed_image).real
print(f'\n\nCorrelation coefficient = {correl_coef}')


""" Images entropy calculation """
H1 = calcEntropy2dSpeedUp(vd_image, 3, 3)
print('\nH = ', H1)

opencv.waitKey(0)
opencv.destroyAllWindows()
