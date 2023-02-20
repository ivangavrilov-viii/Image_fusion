import cv2

# Load the image
img = cv2.imread('image.jpg')

# Apply a median filter with kernel size 5
img_median = cv2.medianBlur(img, 5)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Median Filtered Image', img_median)
cv2.waitKey(0)
cv2.destroyAllWindows()