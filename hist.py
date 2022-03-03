import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\anand\\Pictures\\image1.jpg")
#############2 D Histogram using cv2 ###########################################
#imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#hist=cv2.calcHist([imghsv],[0,1],None,[180,256],[0,180,0,256])
#plt.imshow(hist,interpolation='nearest')
#plt.show()

############Histogram using Open cv outline visible#############################
#col=('b','g','r')
#for i in range(0,3):
#    plot1=cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(plot1,col[i])
#    plt.xlim([0,256])
#plt.show()
############Histogram using Matplotlib Bar graph#############################
#plt.hist(img[:,:,0].ravel(),256,[0,256])
#plt.hist(img[:,:,1].ravel(),256,[0,256])
#plt.hist(img[:,:,2].ravel(),256,[0,256])
#plt.show()
#############Histogram equalization not using open Cv############################
#plt.hist(img.ravel(),256,[0,256])
#plt.show()
#hist,bins=np.histogram(img.ravel(),256,[0,256])
#cdf=hist.cumsum()
#cn=hist.max()*cdf/cdf.max()
#plt.plot(cn,color="b")
#plt.hist(img.ravel(),256,[0,256],color="r")
#plt.show()
#############Histogram equalization using open Cv############################
imgrs=cv2.resize(img,(350,500),interpolation=cv2.INTER_AREA)
imghist1=cv2.equalizeHist(imgrs[:,:,0])
imghist2=cv2.equalizeHist(imgrs[:,:,1])
imghist3=cv2.equalizeHist(imgrs[:,:,2])
imghist=cv2.merge([imghist1,imghist2,imghist3])
imggray=cv2.cvtColor(imghist,cv2.COLOR_BGR2GRAY)
imgsobel=cv2.Canny(imggray,100,200)
cv2.imshow("",imgsobel)
cv2.waitKey(0)
cv2.destroyAllWindows()