import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("C:\\Users\\anand\\Pictures\\liberty.jpg",0)
#hist=cv2.calcHist([img],[0],None,[256],[0,226])
##hist,bins=np.histogram(img.ravel(),256,[0,256])
#plt.plot(hist,color='b')
#plt.xlim([0,256])
#plt.show()
#-----------------------------------------------------------
#colo=('b','g','r')     
#for i,col in enumerate(colo):
#    hist=cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(hist,color=col)
#    plt.xlim([0,256])
#plt.show()
#-----------------------------------------------------------
r,c=img.shape
mas=np.zeros((r,c),np.uint8)
mas[int(r/2)-200:int(r/2)+200,int(c/2)-500:int(c/2)+500]=255
maskedimg=cv2.bitwise_and(img,img,mask=mas)
histimag=cv2.calcHist([img],[0],None,[256],[0,256])
histmasim=cv2.calcHist([img],[0],mas,[256],[0,256])
plt.subplot(221)
plt.imshow(img)
plt.subplot(222)
plt.imshow(mas)
plt.subplot(223)
plt.imshow(maskedimg)
plt.subplot(224)
plt.plot(histimag,color='b')
plt.plot(histmasim,color='r')
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()