# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:25:35 2019

@author: Vivek Vishan
"""

import numpy as np

# 1D array
a = np.array([1, 2, 3, 4])
print(a)

type(a)

a.ndim

# 2D array
# 3 X 3
b = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]])
print(b)

b.ndim

b.size

b.shape

b.dtype
# 3D Array
# 3 X 3 X 3
c = np.array([[[1,2,3],[4,5,6],[7,8,9]],
              [[11,12,13],[14,15,16],[17,18,19]],
              [[20,21,22],[23,24,25],[26,27,28]]])

print(c)

#Arange
d = np.arange(10,21)
d

#Zeros
x =np.zeros((3,3),dtype=np.int16)
x

# ones
y=np.ones((4,5),dtype = np.int16)
y

print(x.ndim)

print(c.ndim)

print(c.size)
print(x.size)
print(b.size)
print(b.itemsize)
print(c.itemsize)

print(b.dtype)
print(b.dtype)

print(b.shape)
print(c.shape)


#Reshape

print(a.reshape(2,2))

print(b.reshape(9))