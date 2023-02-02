import cv2 as opencv


def maximum_method(image_1, image_2):
    """ Метод максимума """

    h, w = image_1.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            if image_1[row, column] < image_2[row, column]:
                image_1[row, column] = image_2[row, column]

    return image_1

    # print(type(image_1))
    # print(type(image_2))
    #
    # output_image = list()
    # for i in range(l):
    #     im_1 = int(image_1[i])
    #     im_2 = int(image_2[i])
    #     output_image.append(max(im_2, im_1))
    #
    # return np.ravel(output_image)


def averaging_method(image_1, image_2):
    """ Метод усреднения """

    output_image = image_1
    h, w = output_image.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            output_image[row, column] = round(int(image_1[row, column]) + int(image_2[row, column])) / 2

    return output_image


def mask_method(image_1, image_2):
    """ Метод маски """

    output_image = image_1
    h, w = output_image.shape

    threshold_value = 170

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            if int(image_2[row, column]) >= threshold_value:
                output_image[row, column] = image_2[row, column]

    return output_image


def power_transformation_method(image_1, image_2):
    """ Метод степенного преобразования """
    output_image = image_1
    h, w = output_image.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            power = 1 - (int(image_2[row, column]) / pow(2, 8))
            output_image[row, column] = pow(int(image_1[row, column]), power)

    return output_image


def weight_function_method(image_1, image_2):
    """ Метод весовой функции """

    vd_im = vd_image.flatten()
    ir_im = ir_image.flatten()
    l = len(vd_im)

    sum_vir = sum(ir_im)
    sum_vd = sum(vd_im)

    alfa = sum_vir / (sum_vir + sum_vd)

    output_image = image_1
    h, w = output_image.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            output_image[row, column] = alfa * int(image_1[row, column]) + (1 - alfa) * int(image_2[row, column])

    return output_image


""" Считывание двух исходных изображений в градациях серого """
vd_image = opencv.imread(r'./images/building_photos/TV.PNG', opencv.IMREAD_GRAYSCALE)
ir_image = opencv.imread(r'./images/building_photos/TIR.PNG', opencv.IMREAD_GRAYSCALE)

# """Преобразование двумерного массива пикселей изображений в одномерный"""
# vd_im = vd_image.flatten()
# ir_im = ir_image.flatten()

""" Вывод на экран изображения до комплексирования """
opencv.imshow('VD', vd_image)
opencv.imshow('VIR', ir_image)

""" Вывод изображения, полученного одним из методов комплексирования """
new_image = mask_method(vd_image, ir_image)
opencv.imshow('New Image', new_image)

opencv.waitKey(0)
opencv.destroyAllWindows()
