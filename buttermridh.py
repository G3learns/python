import cv2
o1=cv2.getTickCount()
img=cv2.imread("C:\\Users\\anand\\Pictures\\image2.jpg")
bf=cv2.imread("C:\\Users\\anand\\Pictures\\bfly.png")

r,c,ch=bf.shape
img1=img[0:r,0:c]

grey=cv2.cvtColor(bf,cv2.COLOR_BGR2GRAY)
thres,mask=cv2.threshold(grey,10,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)

bg=cv2.bitwise_and(img1,img1,mask=mask_inv)
fg=cv2.bitwise_and(bf,bf,mask=mask)

imasg=cv2.add(fg,bg)
img[0:r,0:c]=imasg
img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
cv2.imshow("Butterfly",img)
cv2.imwrite("C:\\Users\\anand\\Pictures\\Bflymrid.jpg",img)
o2=cv2.getTickCount()
print((o2-o1)/cv2.getTickFrequency())
cv2.waitKey(0)
cv2.destroyAllWindows()
