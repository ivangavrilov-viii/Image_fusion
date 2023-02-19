from matplotlib import pyplot as plt
#from common import splitfn
import os
img_names_undistort = [img for img in glob.glob('C:/Users/Chuee/Desktop/diplom/kalibrovka/vid/cam_Camera1_cam_20221111181600_1211064.bmp')]
new_path = 'C:/Users/Chuee/Desktop/diplom/kalibrovka'
camera_matrix = np.array([[1.35385364e+03, 0.00000000e+00,9.99186398e+02],
                         [0.00000000e+00, 1.35385852e+03, 5.76342587e+02],
                         [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]);
dist_coefs = np.array([-0.44876128,  0.37527417, -0.0009433,  -0.00097537, -0.48784801]);
i = 0
#for img_found in img_names_undistort:
while i < len(img_names_undistort):
        img = cv2.imread(img_names_undistort[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h,  w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 0, (w, h))
        dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        # crop and save the image
        x, y, w, h = roi
        dst = dst[y:y+h-50, x+70:x+w-20]
        IMG = cv2.imshow("hhhh",dst)
        name = img_names_undistort[i].split("/")
        name = name[6].split(".")
        name = name[0]
        full_name = new_path + name + '.bmp'
        #outfile = img_names_undistort + '_undistorte.bmp'
        print('Undistorted image written to: %s' % full_name)
        cv2.imwrite(full_name, dst)
        i = i + 1
