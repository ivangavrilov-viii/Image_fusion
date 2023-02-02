def dispersion(input_images) -> None:
    """ Функция для расчета значения дисперсии изображения"""

    dispersion_list = list()

    for image in input_images:
        image = image.flatten()
        l = len(image)

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

        dispersion_list.append(sum(list_of_dis))

    print(f'Dispersion VD image: {dispersion_list[0]}')
    print(f'Dispersion IRD image: {dispersion_list[1]}')
    if len(input_images) > 2:
        print(f'Dispersion complexed image: {dispersion_list[2]}')
        print(f'\nDispersion between IRD and complexed images: {abs(dispersion_list[1] - dispersion_list[2])}')
    print(f'Dispersion between VD and complexed images: {abs(dispersion_list[0] - dispersion_list[2])}')

