# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:04:10 2020

@author: anand
"""
import cv2
import numpy as np

img=cv2.imread("C:\\Users\\anand\\Pictures\\j.png")
img1=cv2.GaussianBlur(img,(3,3),0)
img1=cv2.Laplacian(img1,cv2.CV_64F)
res,img2=cv2.threshold(img1,0,255,0)
cv2.imshow("Gaussian Blur",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()