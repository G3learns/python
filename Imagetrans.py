import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("C:\\Users\\anand\\Pictures\\liberty.jpg")
#hits=cv2.calcHist([img],[0],None,[256],[0,256])
#plt.subplot(121)
#plt.plot(hits,color="r")
#plt.xlim([0,255])
#plt.show()
#----------------------------------------------
#r,c=img.shape
#noi=32*np.uint8(np.random.randn(r,c))
#image=cv2.add(img,noi)
#imag=cv2.hconcat([img,image])
#cv2.imshow("Noise",imag)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#-----------------------
mat=np.ones([3,3])*(1/9)
filimag=cv2.filter2D(img,-1,mat)
filimag1=cv2.blur(img,(3,3))
filimag2=cv2.GaussianBlur(img,(3,3),0)
filimag3=cv2.medianBlur(img,5)
plt.subplot(221)
plt.imshow(img)
plt.subplot(222)
plt.imshow(filimag)
plt.subplot(223)
plt.imshow(filimag1)
plt.subplot(224)
plt.imshow(filimag2)
#cv2.imshow("Noise",filimag1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()