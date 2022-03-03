import cv2
import numpy as np

img=cv2.imread("C:\\Users\\anand\\Pictures\\liberty.jpg",0)
mat=np.array([[1,0,-1],
              [2,0,-2],
              [1,0,-1]])
img1=cv2.filter2D(img,-1,mat)
for i in mat:
    for j in i:
        if j<0:
            j=-j
thres,img2=cv2.threshold(img,127,255,0)
#img2=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
cv2.imshow("Filtered",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
