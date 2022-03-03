import cv2
import numpy as np
#edge detection
#img=cv2.imread("C:\\Users\\anand\\Pictures\\images.jfif")
#im1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edge=cv2.Canny(im1,100,200)
#im,con,hier=cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#cn=cv2.drawContours(img,con,-1,(0,255,0),2)
#cv2.imshow("",cn)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#find contour
img=cv2.imread("C:\\Users\\anand\\Pictures\\ayah.jpg",0)
r,c=img.shape
#ihsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#print(ihsv[int(1000),int(2000),:])
#lred=np.array([150,0,0])
#hred=np.array([200,255,255])
#irose=cv2.inRange(ihsv,lred,hred)
#suc,ithre=cv2.threshold(img,127,255,0)
#edge=cv2.Canny(ithre,10,200)
roed,contour,hier=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
icon=cv2.drawContours(img,contour,-1,(0,255,0),20)
cv2.imshow("Image",icon)
cv2.waitKey(0)
cv2.destroyAllWindows()
