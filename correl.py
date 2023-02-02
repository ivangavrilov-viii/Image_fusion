import cv2 as opencv
import math


def correlation_coefficient(image_1, image_2, l: int) -> float:
    """ Функция для расчета коэффициента корреляции для двух изображений,
    где l - длина одномерного массива изображения (одинаковая для двух изображений,
    т.к. они должны быть одного размера"""

    sum_im_1 = 0
    sum_im_2 = 0
    sum_all_im = 0
    squareSum_im_1 = 0
    squareSum_im_2 = 0

    for i in range(l):
        im_1 = int(image_1[i])
        im_2 = int(image_2[i])
        sum_im_1 += im_1
        sum_im_2 += im_2
        sum_all_im += im_1 * im_2
        squareSum_im_1 += pow(im_1, 2)
        squareSum_im_2 += pow(im_2, 2)

    coef = (l * sum_all_im - sum_im_1 * sum_im_2) / (
        math.sqrt((l * squareSum_im_1 - sum_im_1 * sum_im_1) * (l * squareSum_im_2 - sum_im_2 * sum_im_2)))
    return coef


""" Считывание двух сравниваемых изображений """
image_vd = opencv.imread('./images/science_article/VD.jpg', opencv.IMREAD_GRAYSCALE)
image_complex = opencv.imread('./images/science_article/complex.png', opencv.IMREAD_GRAYSCALE)

"""Преобразование двумерного массива пикселей изображений в одномерный"""
im1 = image_vd.flatten()
im2 = image_complex.flatten()

"""Использование функции расчета коэффициента корреляции с его последующим выводом"""
print(f'Correlation coefficient: {correlation_coefficient(im1, im2, len(im1)).real}')
