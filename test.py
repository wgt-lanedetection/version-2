import numpy as np
import cv2

point_ul =  45,182
point_ol = 107,117
point_or = 213,117
point_ur = 288,182


def perspective_transform(img):
    """
    Execute perspective transform
    """
    img_size = (img.shape[1], img.shape[0])
    src = np.float32([[45,182],[107,117],[213,117],[288,182]])
    dst = np.float32([[71,182],[71,0],[270,182]])

    m = cv2.getPerspectiveTransform(src, dst)
    m_inv = cv2.getPerspectiveTransform(dst, src)

    warped = cv2.warpPerspective(img, m, img_size, flags=cv2.INTER_LINEAR)
    unwarped = cv2.warpPerspective(warped, m_inv, (warped.shape[1], warped.shape[0]), flags=cv2.INTER_LINEAR)  # DEBUG

    return warped #, unwarped, m, m_inv

def test(txt):
    printf(txt)

image = cv2.imread('lane.png')
#image = cv2.resize(image, (int(320), int(192)))
warped = perspective_transform(image)
cv2.imshow('Unwarped',unwarped)
cv2.imshow('Warped', warped)
