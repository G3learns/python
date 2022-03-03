import cv2
import numpy as np
def gn(r,c):
    nimg=0.7*np.random.randn(r,c)
    print(nimg[1,:])
    return np.uint8(nimg)

yy=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg",0)
r,c=yy.shape
ad1=cv2.add(yy,gn(r,c))
cv2.imshow("image",ad1)
cv2.waitKey(0)
cv2.destroyAllWindows()