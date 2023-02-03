# from skimage.io import imread, imshow, imsave
# from skimage import img_as_float, img_as_ubyte
# from numpy import histogram as hist
# from numpy import dstack
# import numpy as np
#
# import warnings
#
# warnings.filterwarnings("ignore")
#
# global name, ims
#
# im = [0, 0, 0]
# impr = [0, 0, 0]
#
# # ���������
# # � ����� � ���������� ������ ������ ����������� ���� 0.jpg, 1.jpg... 99999.jpg
# pix = 1  # ����� �������� � ����� ��� ���������
# ext = ('png')  # ��� ������� ������
# extout = ('png')  # ��� ��������
# img_center = 1  # ��������� �������
# img_hist = 1  # ������������ ������������
# save_pic = 0  # ������� ��������� ��������
# save_stack = 1  # ������� ��������� ��������
#
#
# # ���������� ������� �� ������� � ������,
# # �� ���� ������� �������� ����� ������, ��� �������� � ������������� ��������
# def chan(n, img, shift):
#     img = np.fft.fft2(img[:, :, n])
#     if shift == 1:
#         img = np.fft.fftshift(img)  # ��������� �������
#     return img
#
#
# def comp(ims, shift, align):
#     """ Обработка всех каналов картинки """
#
#     for i in (0, 1, 2):
#         im[i] = np.log(1 + abs(chan(i, ims, shift)))  # �������� ������������ ��� �������
#         im[i] = im[i] / im[i].max()  # ��������������� �������
#
#         if align == 1:  # ������������ �����������
#             imt = img_as_ubyte(im[i])
#             iy, ix = imt.shape
#             values, bin_edges = hist(imt.ravel(), bins=range(257))
#             for k in range(257):
#                 cdf = np.cumsum(values[:k])
#             count = 0
#             for m in range(256):
#                 count += cdf[m]
#                 if count > 0:
#                     x_min = i
#                     break
#             cdfmin = cdf[x_min:].min()
#             imt = np.round((cdf[imt] - cdfmin) / (iy * ix - 1) * 255)
#             imt = np.array(imt, dtype=np.uint8)
#             im[i] = imt
#
#     impr = dstack((im[0], im[1], im[2]))  # ����������� �������
#     return impr
#
#
# for p in range(pix):
#     cap = p
#     name = str(cap) + '.' + ext
#     ims = imread(name)
#     if ims.shape[2] > 2:
#         ims = dstack((ims[:, :, 0], ims[:, :, 1], ims[:, :, 2]))
#
#     # ������������ ������������� �������: �����������, �����, ������������ ����������
#     impr1 = comp(ims, img_center, img_hist)
#
#     # ���������� ������������ �������
#     if save_pic == 1:
#         imsave('export-' + str(cap) + '.' + extout, impr1)
#
#     # ���������� ��������� �������� � �������
#     if save_stack == 1:
#         if impr1.shape[0] >= impr1.shape[1]:
#             imsave('stack-' + str(cap) + '.' + extout, np.hstack((ims, impr1)))
#         else:
#             imsave('stack-' + str(cap) + '.' + extout, np.vstack((ims, impr1)))
#
#     # imsave('export-'+str(cap)+'-st2.'+ext, np.hstack((imread(name),'export-'+str(cap)+'.'+extout)))
#
#     # Строка состояния
#     print("\r", name + ' - OK!', end=" ")
#
# print(' === COMPLETE ===')
