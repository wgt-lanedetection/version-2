import numpy as np
import cv2
import pickle

point_ul =  45,182
point_ol = 107,117
point_or = 213,117
point_ur = 288,182


def perspective_transform(img):
	"""
	Execute perspective transform
	"""
	img_size = (img.shape[1], img.shape[0])

        src = np.float32(
                            [[ point_ul], #Punkt unten Links
                            [  point_ol], #Punkt oben Links
                            [  point_or], #Punkt oben Rechts
                            [  point_ur]])#Punkt unten Rechts
        dst = np.float32(
                            [[ 71,   182], #Punkt unten Links
                            [  71,     0], #Punkt oben Links
                            [ 250,     0], #Punkt oben Rechts
                            [ 270,   182]])#Punkt unten Rechts
                

	m = cv2.getPerspectiveTransform(src, dst)
	m_inv = cv2.getPerspectiveTransform(dst, src)

	warped = cv2.warpPerspective(img, m, img_size, flags=cv2.INTER_LINEAR)
	unwarped = cv2.warpPerspective(warped, m_inv, (warped.shape[1], warped.shape[0]), flags=cv2.INTER_LINEAR)  # DEBUG

	return warped, unwarped, m, m_inv

image = cv2.imread(image.png)
image = cv2.resize(image, (int(320), int(192)))
warped = perspective_transform(image)
cv2.imshow('Unwarped',unwarped)
cv2.imshow('Warped', warped)
