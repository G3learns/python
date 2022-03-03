import cv2
import numpy as np
img = cv2.imread("C:\\Users\\anand\\Pictures\\chessboard.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst=np.float32(gray)
dst=cv2.cornerHarris(dst,2,3,0.04)
dst=cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,255,0]
cv2.imshow("corner",img)
cv2.waitKey(0)
cv2.destroyAllWindows()