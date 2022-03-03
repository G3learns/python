import cv2
import numpy as np
img=cv2.imread("C:\\Users\\anand\\Pictures\\liberty.jpg")
hst=cv2.calcHist([img.flatten()],[0],None,[256],[0,256])
cdf=hst.cumsum()
print(hst)
cdf_normal=cdf*hst.max()/cdf.max()
