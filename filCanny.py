import cv2
img=cv2.imread("C:\\Users\\anand\\Pictures\\liberty.jpg",0)
img1=cv2.Canny(img,100,200)
cv2.imshow("Canny",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()