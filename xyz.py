import cv2
import numpy as np

img=cv2.imread("C:\\Users\\anand\\Pictures\\image1.jpg")
imgre=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
imgxyz=cv2.cvtColor(imgre,cv2.COLOR_BGR2XYZ)
#col,row,ch=imgxyz.shape
#brightne=np.ones((col,row),np.uint8)
#brightne*=100

imgxyz[:,:,2]=imgxyz[:,:,2]*2
imgbgr=cv2.cvtColor(imgxyz,cv2.COLOR_XYZ2BGR)
cv2.imshow("xyz",imgbgr)
cv2.waitKey(0)
cv2.destroyAllWindows()