
#('C:/Users/Chuee/Desktop/diplom/kalibrovka/ik/cam_Camera2_cam_20221111184048_2698926.bmp')
#('C:/Users/Chuee/Desktop/diplom/kalibrovka/vid/cam_Camera1_cam_20221111181547_1198501.bmp')

import cv2
import numpy as np

# Load the images
ir_img= cv2.imread('C:/Users/Chuee/Desktop/diplom/test_ik.png')
color_img = cv2.imread('C:/Users/Chuee/Desktop/diplom/test_vid.png')
cv2.imshow('IR',ir_img)
cv2.imshow('VID', color_img)
# Convert images to grayscale
ir_gray = cv2.cvtColor(ir_img, cv2.COLOR_BGR2GRAY)
color_gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# Detect keypoints and compute descriptors
kp1, des1 = sift.detectAndCompute(ir_gray, None)
kp2, des2 = sift.detectAndCompute(color_gray, None)
print('key point for ir',kp1)
print('key point for color',kp2)
# Match keypoints using FLANN matcher
matcher = cv2.FlannBasedMatcher()
matches = matcher.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x:x.distance)

# Keep only the best matches
num_best_matches = int(len(matches) * 0.1)
matches = matches[:num_best_matches]

# Extract the matched keypoints
src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)

# Estimate homography using RANSAC algorithm
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Warp the color image to the IR image using the homography
warped_color = cv2.warpPerspective(color_img, H, (ir_img.shape[1], ir_img.shape[0]))

# Blend the warped color image and the IR image using alpha blending
alpha = 0.5
beta = 1 - alpha
overlay = cv2.addWeighted(ir_img, alpha, warped_color, beta, 0)

# Show the result
cv2.imshow('Overlay', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()