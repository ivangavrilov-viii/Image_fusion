import numpy as np
from matplotlib import pyplot as plt


def fourier_transform(input_image):
    f = np.fft.fft2(input_image)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    # count = 0
    # new_list = list()
    # for string in magnitude_spectrum:
    #     for pixel in string:
    #         count += 1
    #         new_list.append(np.uint8(pixel))
    #         if count == 10:
    #             break
    #     break

    # print(new_list)
    # etalon_list = list()
    # for elem in [0, 50, 100, 150, 200.452342, 255, 300.4545454]:
    #     etalon_list.append(np.uint8(elem))
    # print(etalon_list)


    plt.subplot(121), plt.imshow(input_image, cmap='gray')
    plt.title('Input Image')
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum')
    plt.show()

    new_image = list()
    h, w = input_image.shape
    for i in range(h):
        for j in range(w):
            if magnitude_spectrum[i][j] > 255:
                new_element = 255
                new_element = np.uint8(new_element)
            else:
                new_element = np.uint8(magnitude_spectrum[i][j])
            new_image.append(new_element)

    return np.reshape(new_image, (h, w))
