# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:49:55 2021

@author: anand
"""

import cv2
import numpy as np

img=cv2.imread("C:\\Users\\anand\\Pictures\\image.jpg")
r,c=img.shape[:2]
rot_mat=cv2.getRotationMatrix2D((c/2,r/2),90,1)
trans_imag=cv2.warpAffine(img,rot_mat,(r,c))
cv2.imshow("",trans_imag)
cv2.waitKey()
cv2.destroyAllWindows()