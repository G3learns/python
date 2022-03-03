import cv2
import numpy as np
img=cv2.imread("C:\\Users\\anand\\Pictures\\water_coins.jpg")
imgbw=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
r,thres=cv2.threshold(imgbw,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
ker=np.ones((3,3),np.uint8)
imgo=cv2.morphologyEx(thres,cv2.MORPH_OPEN,ker,iterations=2)
imgbg=cv2.dilate(imgo,ker,iterations=3)
imgdt=cv2.distanceTransform(imgbg,cv2.DIST_L2,5)
r,thres=cv2.threshold(imgdt,0.7*imgdt.max(),255,0)
imgfg=np.uint8(thres)
unknown=cv2.subtract(imgbg,imgfg)
t,marker=cv2.connectedComponents(imgfg)
marker=marker+1
marker[unknown==255]=0
marker=cv2.watershed(img,marker)
img[marker==-1]=[0,255,0]
cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()