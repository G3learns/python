import cv2
import numpy as np
image=cv2.imread("C:\\Users\\anand\\Pictures\\snap2.jpg")
picture=cv2.imread("C:\\Users\\anand\\Pictures\\GayathriT1.jpg")
picture=cv2.resize(picture,(image.shape[1],image.shape[0]),interpolation=cv2.INTER_AREA)
img=image.copy()
A=[img]
for i in range(5):
    img=cv2.pyrDown(img)
    A.append(img)
pic=picture.copy()
B=[pic]
for i in range(5):
    pic=cv2.pyrDown(pic)
    B.append(pic)
LpyA=[A[5]]
for i in range(5,0,-1):
    size=(A[i-1].shape[1],A[i-1].shape[0])
    G=cv2.pyrUp(A[i],dstsize=size)
    L=cv2.subtract(A[i-1],G)
    LpyA.append(L)
LpyB=[B[5]]
for i in range(5,0,-1):
    size=(B[i-1].shape[1],B[i-1].shape[0])
    G=cv2.pyrUp(B[i],dstsize=size)
    L=cv2.subtract(B[i-1],G)
    LpyB.append(L)
LS=[]
for la,lb in zip(LpyA,LpyB):
    r,c,ch=la.shape
    h=int(c//2)
    imge=np.hstack((la[:,0:h],lb[:,h:]))
    LS.append(imge)
Final=LS[0]
for i in range(1,6):
    size=(LS[i].shape[1],LS[i].shape[0])
    Final=cv2.pyrUp(Final,dstsize=size)
    Final=cv2.add(Final,LS[i])
cv2.imshow("",Final)
cv2.waitKey(0)
cv2.destroyAllWindows()
