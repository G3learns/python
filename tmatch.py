import cv2
import numpy as np
def imagematch(img,timg):
    h,w=timg.shape
    res=cv2.matchTemplate(img,timg,cv2.TM_SQDIFF)
    t_min,t_max,t_miloc,t_maloc=cv2.minMaxLoc(res)
    topleft=t_miloc
    bottomright=(topleft[0]+w,topleft[1]+h)
    sq=cv2.rectangle(img,topleft,bottomright,255,2)
    return sq
def manyimagematch(img,timg):
    h,w=timg.shape
    res=cv2.matchTemplate(img,timg,cv2.TM_CCOEFF_NORMED)
    loc=np.where(res>=0.4)
    for pt in zip(*loc[::-1]):
        sq=cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),255,2)
    return sq
    
img=cv2.imread("C:\\Users\\anand\\Pictures\\airplane.jpeg",0)
timg=cv2.imread("C:\\Users\\anand\\Pictures\\tair.jpeg",0)
sq=manyimagematch(img,timg)
cv2.imshow("",sq)
cv2.waitKey(0)
cv2.destroyAllWindows()