# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:54:12 2020

@author: anand
"""

import tensorflow as tf
t1=tf.Variable(1,tf.int32)
t2=tf.Variable([[[[1,2,3],[1,2,4],[1,2,5]],[[1,2,3],[1,2,4],[1,2,5]],\
                 [[1,2,3],[1,2,4],[1,2,5]]]],tf.string)
t4=tf.ones((1,2,3),tf.int32)
print(tf.shape(t2))
#t3=tf.reshape(t2,(3,3))
print(t2.shape)
print(t4)
with tf.Session() as sess:
    t1.eval()