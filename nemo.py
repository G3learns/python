import cv2
import matplotlib.pyplot as plt
yy=cv2.imread("C:\\Users\\anand\\Pictures\\np.jpg",0)
#yy=cv2.medianBlur(yy,5)
#t1=cv2.adaptiveThreshold(yy,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#t2=cv2.adaptiveThreshold(yy,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
r,t1=cv2.threshold(yy,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
yy=cv2.GaussianBlur(yy,(5,5),0)
r,t2=cv2.threshold(yy,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Title=["Original","Adaptive Mean","Adaptive Gaussian"]
images=[yy,t1,t2]
for i in range(3):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(Title[i])
plt.show()
cv2.imshow("Figure",t2)
cv2.waitKey(0)
cv2.destroyAllWindows()