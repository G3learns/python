# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:49:22 2021

@author: anand
"""

import numpy as np
from matplotlib import pyplot as plt

#x1=np.linspace(-10.0,10.0,100)
#x2=np.linspace(-10.0,10.0,100)
#plt.scatter(x1,x2)
#plt.show
#
#a=[1,2,3]
#a3,a4=np.meshgrid(a,a)
#print(a3,a4)

#x=np.arange(1,20,2)
w=np.linspace(-10.0,10.0,100)
b=np.linspace(-10.0,10.0,100)
X1,X2=np.meshgrid(w,b)
Y=np.sqrt(np.square(X1) + np.square(X2))
cm=plt.cm.get_cmap('viridis')
plt.scatter(X1, X2, c=Y, cmap=cm)
plt.show()