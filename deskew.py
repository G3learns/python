import numpy as np
import cv2
SZ=20
affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR
bins=16
#svm_param=dict(kernel_type=cv2.SVM_LINEAR,svm_type=cv2.SVM_C_SVC,C=2.67,gamma=5.383)

def deskew(img):
    m=cv2.moments(img)
    if m['mu02']<1e-2:
        return img.copy()
    sk=m['mu11']/m['mu02']
    M=np.float32([[1,sk,-0.5*SZ*sk],[0,1,0]])
    img1=cv2.warpAffine(img,M,(10,20),flags=cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR)
    return img1
def hog(img):
    
    sx=cv2.Sobel(img,cv2.CV_32F,1,0)
    sy=cv2.Sobel(img,cv2.CV_32F,0,1)
    mag,ang=cv2.cartToPolar(sx,sy)
    bin_s=np.int32(bins*ang/(2*np.pi))
    bina=bin_s[:10,:10],bin_s[:10,10:],bin_s[10:,:10],bin_s[10:,10:]
    maga=mag[:10,:10],mag[:10,10:],mag[10:,:10],mag[10:,10:]
    hists=[np.bincount(b.ravel(),m.ravel(),bins)for b,m in zip(bina,maga)]
    hist=np.hstack(hists)
    return hist
    
fullimg=cv2.imread('C:\\Users\\anand\\Pictures\\digits.png',0)
print(fullimg.shape)
cells=[np.vsplit(row,50) for row in np.hsplit(fullimg,100)]
print(np.array(cells).shape)
data=[j for i in cells for j in i]
traindata=data[:2500]
testdata=data[2500:]
cv2.imshow("",cv2.resize(traindata[49],(30,60),fx=3,fy=3,interpolation=cv2.INTER_CUBIC))
cv2.waitKey(0)
cv2.destroyAllWindows()
print(np.array(traindata).shape)
a=[]
for i in traindata:
    ske=deskew(i)
    hogi=hog(ske)
    a.append(hogi)
print(np.array(a).shape)
traind=np.float32(a)
trainr=np.repeat(np.arange(10),5)
trainr=np.float32(trainr*50)
trainr=trainr[:,np.newaxis]
testr=np.copy(trainr)
print(trainr[49])
a1=[]
for i in testdata:
    ske1=deskew(i)
    hogi1=hog(ske1)
    a1.append(hogi1)
print(np.array(a1).shape)
testd=np.float32(a1)
knn=cv2.ml_KNearest.create()
knn.train(traind,cv2.ml.ROW_SAMPLE,trainr)
re,result,neigh,dist=knn.findNearest(testd,k=5)
match=result==testr
cou=np.count_nonzero(match)
accuracy=cou*100/result.size
print(accuracy)


