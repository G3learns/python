import cv2
#import numpy as np
img=cv2.imread("C:\\Users\\anand\\Pictures\\chessboard.jpg")
imgbw=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corner=cv2.goodFeaturesToTrack(imgbw,80,0.01,10)
for i in corner:
    x,y=i.ravel()
    cv2.circle(img,(x,y),2,[0,255,0],2)
cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()