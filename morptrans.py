import cv2
yy=cv2.imread("C:\\Users\\anand\\Pictures\\Liberty.jpg")
edg=cv2.Canny(yy,100,200)
cv2.imshow("Edge",edg)
cv2.waitKey(0)
cv2.destroyAllWindows()