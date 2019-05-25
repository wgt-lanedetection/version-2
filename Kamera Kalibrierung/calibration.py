import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import glob
import pickle as pickle

nx = 9
ny = 6

objp = np.zeros((nx * ny, 3), np.float32)
objp[:,:2] = np.mgrid[0: nx, 0: ny].T.reshape(-1, 2)


# create lists to store imagepoints and objectpoints
objpoints = []
imgpoints = []


plt.figure(figsize = (20, 5))
plt.title('calibration')


for i in range(20):
    fname = '/home/pi/lane/calibration/pictures/calibration' + str(i+1) + '.jpg'
    img = cv2.imread(fname)
    
    # grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.subplot(4, 5, i+1)
    # Find corners of chessboard, (we had to grayscale first to find them)
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    if ret == True:
        # draw corners onto the original image
        cv2.drawChessboardCorners(img, (nx, ny), corners, ret)

        objpoints.append(objp)
        imgpoints.append(corners)

        plt.imshow(img)
    else:
        plt.imshow(img)
    plt.axis('off')

# pick the first image to use its size

fname = 'camera_cal/calibration1.jpg'
img = mpimg.imread(fname)
img_size = (img.shape[1], img.shape[0])
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)

# Die errechneten Matrizen für die Entzerrungsfunktion

print(mtx)
print(dist)
