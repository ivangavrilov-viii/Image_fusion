def maximum_method(image_1, image_2):
    """ Метод максимума """

    h, w = image_1.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            if image_1[row, column] < image_2[row, column]:
                image_1[row, column] = image_2[row, column]

    return image_1


def averaging_method(image_1, image_2):
    """ Метод усреднения """

    output_image = image_1
    h, w = output_image.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            output_image[row, column] = round(int(image_1[row, column]) + int(image_2[row, column])) / 2

    return output_image


def mask_method(image_1, image_2, input_threshold):
    """ Метод маски """

    output_image = image_1
    h, w = output_image.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            if int(image_2[row, column]) >= input_threshold:
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

    vd_im = image_1.flatten()
    ir_im = image_2.flatten()

    sum_vir = sum(ir_im)
    sum_vd = sum(vd_im)

    alfa = sum_vir / (sum_vir + sum_vd)

    output_image = image_1
    h, w = output_image.shape

    for row in range(2, h - 2):
        for column in range(2, w - 2):
            output_image[row, column] = alfa * int(image_1[row, column]) + (1 - alfa) * int(image_2[row, column])

    return output_image
