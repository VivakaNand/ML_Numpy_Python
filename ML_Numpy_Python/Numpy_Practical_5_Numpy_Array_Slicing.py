# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:21:45 2019

@author: Vivek Vishan
"""

import numpy as np

mx = np.arange(1,101).reshape(10,10)
print(mx)

mx[0,0]

mx[0,0].ndim

mx[0]

mx[:,0]


mx[:,0:1]


mx[:,0:1].ndim

mx[1:4,1:4]

mx[:,1:3]

mx[:]

mx[::]

mx[:,:]

mx.itemsize

mx.dtype