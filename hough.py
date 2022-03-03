import cv2
import numpy as np

img=cv2.imread("C:\\Users\\anand\\Pictures\\circle.png",0)
img=cv2.medianBlur(img,5)
imgg=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#imgbw=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edg=cv2.Canny(imgbw,50,150,apertureSize=3)
# =============================================================================
#Hough Line TRansform
# lin=cv2.HoughLines(edg,1,np.pi/180,200)
# for lines in lin:
#     for rho,theta in lines:
#         a=np.cos(theta)
#         b=np.sin(theta)
#         x0=rho*a
#         y0=rho*b
#         x1=int(x0+1000*(-b))
#         y1=int(y0+1000*(a))
#         x2=int(x0-1000*(-b))
#         y2=int(y0-1000*(a))
#         cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# =============================================================================
# =============================================================================
# Hough Probability Line transform
# lin=cv2.HoughLinesP(edg,1,np.pi/180,100,100,10)
# for i in lin:
#     for x1,y1,x2,y2 in i:
#         cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)
# cv2.imshow("",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================
#Hough Circle TRanform
cir=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
cir=np.uint8(np.around(cir))
for i in cir[0,:]:
    cv2.circle(imgg,(i[0],i[1]),i[2],255,2)
print(imgg.shape)
cv2.imshow("",imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()