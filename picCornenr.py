import cv2
import numpy as np
img=cv2.imread("C:\\Users\\anand\\Pictures\\chessboard.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
crn=cv2.cornerHarris(gray,2,3,0.04)
crn=cv2.dilate(crn,None)
img[crn>0.01*crn.max()]=[0,0,255] 
cv2.imshow("Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()