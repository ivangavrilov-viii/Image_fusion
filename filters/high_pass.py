import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Subtract the blurred image from the grayscale image to get the high-pass filtered image
high_pass = cv2.subtract(gray, blurred)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('High-Pass Filtered Image', high_pass)
cv2.waitKey(0)
cv2.destroyAllWindows()