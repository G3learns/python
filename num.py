import numpy as np

a = np.arange(12).reshape(3,4)
i = np.array([[0, 1],[1, 2]])
j = np.array([[2, 1],[3, 3]])
data = np.sin(np.arange(20)).reshape(5,4) 
print(data)
ind = data.argmax(axis=0)
print(ind)
i=np.arange(0,12).reshape((3,4))
j=i>4
i[j]=0
print(i)
#[[2,5],[7,1 q1]]

