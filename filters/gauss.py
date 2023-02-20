import cv2 

# Load the image 
img = cv2.imread('image.jpg') 

# Apply a Gaussian filter with kernel size 5 and standard deviation 0 

img_blur = cv2.GaussianBlur(img, (5, 5), 0) 

# Display the original and filtered images 
cv2.imshow('Original Image', img) 

cv2.imshow('Blurred Image', img_blur) 

cv2.waitKey(0) 

cv2.destroyAllWindows()