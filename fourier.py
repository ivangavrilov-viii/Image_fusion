import numpy as np
from matplotlib import pyplot as plt


def fourier_transform(input_image):
    f = np.fft.fft2(input_image)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    # plt.subplot(121), plt.imshow(input_image, cmap='gray')
    # plt.title('Input Image')
    # plt.subplot(122),plt.imshow(magnitude_spectrum, cmap='gray')
    # plt.title('Magnitude Spectrum')
    # plt.show()

    new_image = list()
    h, w = input_image.shape
    for i in range(h):
        magnitude_spectrum[i].astype('uint8')
        for j in range(w):
            new_element = np.uint8(magnitude_spectrum[i][j])
            new_image.append(new_element)

    return np.reshape(new_image, (h, w))
