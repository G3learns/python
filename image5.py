import cv2
import numpy as np
import matplotlib.pyplot as plt 
img1=cv2.imread("C:\\Users\\anand\\Pictures\\image2.jpg")
img2=cv2.imread("C:\\Users\\anand\\Pictures\\images.jfif")
img1=cv2.resize(img1,(500,800),interpolation=cv2.INTER_NEAREST)
img2=cv2.resize(img2,(500,800),interpolation=cv2.INTER_NEAREST)
img3=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow("image",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()