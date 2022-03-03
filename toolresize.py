import cv2
import os
im=cv2.imread('C:\\Users\\anand\\Downloads\\aadhar.jpg',0)
imr=cv2.resize(im,(0,0),fx=0.12,fy=0.12,interpolation=cv2.INTER_AREA)
cv2.imwrite('C:\\Users\\anand\\Desktop\\marks and degree\\aadhar.jpg',imr)
#path='C:\\Users\\anand\\Desktop\\marks and degree\\PG'
#for i in os.listdir(path):
#    im=cv2.imread(os.path.join(path,i))
#    if im is not None:
#        imr=cv2.resize(im,(0,0),fx=0.20,fy=0.20,interpolation=cv2.INTER_AREA)
#        cv2.imwrite('C:\\Users\\anand\\Desktop\\marks and degree\\PG1\\'+i,imr)