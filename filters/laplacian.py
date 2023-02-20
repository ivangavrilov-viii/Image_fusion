import cv2

import numpy as np

# Load the image

img = cv2.imread('image.jpg', 0)

# Apply Laplacian filter with kernel size 3

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

# Display the original and filtered images

cv2.imshow('Original Image', img)

cv2.imshow('Laplacian Filtered Image', laplacian)

cv2.waitKey(0)

cv2.destroyAllWindows()