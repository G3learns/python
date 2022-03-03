import cv2
import numpy as np
a=cv2.imread("C:\\Users\\anand\\Pictures\\ayah.jpg",0)
k=np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]],np.uint8)
a=cv2.GaussianBlur(a,(3,3),0)
kf0=cv2.filter2D(a,cv2.CV_64F,k)
kf=cv2.Sobel(a,cv2.CV_64F,1,0,7)
kf1=cv2.Laplacian(a,cv2.CV_64F,3)
kf2=cv2.Canny(a,100,200)
kf3=a-kf0
cv2.imshow("",kf3)
cv2.waitKey(0)
cv2.destroyAllWindows()