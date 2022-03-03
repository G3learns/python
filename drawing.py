import cv2
import numpy as np
yy=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg")
r,c,ch=yy.shape
pt1=np.float32([[100,10],[200,50],[300,300],[500,750]])
pt2=np.float32([[0,110],[100,150],[200,400],[300,850]])
M=cv2.getPerspectiveTransform(pt1,pt2)
img=cv2.warpPerspective(yy,M,(c,r))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()