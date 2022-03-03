import cv2
import numpy as np

fullimg=cv2.imread('C:\\Users\\anand\\Pictures\\digits.png')
fullimg=cv2.cvtColor(fullimg,cv2.COLOR_BGR2GRAY)
cells=[np.hsplit(row,100) for row in np.vsplit(fullimg,50)]
x=np.array(cells)
traindata = x[:,:50].reshape(-1,200).astype(np.float32)
testdata = x[:,50:100].reshape(-1,200).astype(np.float32)
k=np.arange(10)
trainlabel=np.repeat(k,250)[:,np.newaxis]
testlabel=np.copy(trainlabel)
knn=cv2.ml_KNearest.create()
knn.train(traindata,cv2.ml.ROW_SAMPLE,trainlabel)
ret,result,neigh,dist=knn.findNearest(testdata,k=5)
match=result==testlabel
count=np.count_nonzero(match)
accuracy=count*100.0/result.size
print(accuracy)