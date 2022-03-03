import cv2
import numpy as np
def imageconv(img):
    #return cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    return img
yy=cv2.imread("C:\\Users\\anand\\Pictures\\sn1.jpg")
#M1=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
M=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img1=imageconv(cv2.filter2D(yy,-1,M))
img2=imageconv(cv2.blur(yy,(5,5)))
img3=imageconv(cv2.medianBlur(yy,5))
#img4=imageconv(cv2.GaussianBlur(yy,(5,5),0))
img5=cv2.bilateralFilter(yy,9,75,75)
img4=cv2.medianBlur(img1,5)
#yy=cv2.resize(yy,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
x=[[yy,img1],[img2,img3],[img4,img5]]
final=cv2.vconcat([cv2.hconcat(i) for i in x])
cv2.imshow("Both",final)
cv2.waitKey(0)
cv2.destroyAllWindows()