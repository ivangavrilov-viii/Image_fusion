import cv2 as opencv
import time


def dispersion(image, l: int) -> float:
    """ Функция для расчета значения дисперсии изображения"""
    list_of_dis = list()
    image = tuple(image)
    dict_of_brightness = dict()
    min_brightness = min(image)
    max_brightness = max(image)

    for value in range(min_brightness, max_brightness + 1):
        dict_of_brightness[value] = 0

    for pixel in image:
        dict_of_brightness[pixel] += 1

    for value, count in dict_of_brightness.items():
        value = int(value)
        expected_value = pow(value, 2) * count / l
        list_of_dis.append(expected_value)

    dispersion_of_image = sum(list_of_dis)
    return dispersion_of_image


""" Считывание двух сравниваемых изображений """
image_vd = opencv.imread('./images/science_article/VD.jpg', opencv.IMREAD_GRAYSCALE)
image_complex = opencv.imread('./images/science_article/complex.png', opencv.IMREAD_GRAYSCALE)

# vd_image = opencv.imread(r'./images/building_photos/TV.PNG', opencv.IMREAD_GRAYSCALE)
# ir_image = opencv.imread(r'./images/building_photos/TIR.PNG', opencv.IMREAD_GRAYSCALE)

"""Преобразование двумерного массива пикселей изображений в одномерный"""
im1 = image_vd.flatten()
im2 = image_complex.flatten()

"""Использование функции расчета коэффициента корреляции с его последующим выводом"""
dis_1 = dispersion(im1, len(im1))
dis_2 = dispersion(im2, len(im2))

"""Вывод результата программы в панель пользователя"""
print(f'Dispersion VD image: {dis_1}')
print(f'Dispersion complexed image: {dis_2}')
print(f'Dispersion between images: {abs(dis_1 - dis_2)}')
