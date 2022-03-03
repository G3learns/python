# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:34:00 2021

@author: anand
"""

import numpy as np

def relu(x):
    x=[i for i in x if i>0 else 0]
        
x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[1],[1],[0]])
W=np.random.randn(4,4)
c=np.zeros((4,1))
a=np.dot(W.T,x)+c
h=relu(a)

print(fx)