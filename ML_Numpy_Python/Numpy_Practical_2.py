# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:16:25 2019

@author: Vivek Vishan
"""

import numpy as np

mx_1s = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(mx_1s)


mx_1s = np.ones(5)
print(mx_1s)

mx_1s.dtype

mx_1s = np.ones((3,4))
print(mx_1s)

mx_1s = np.ones((3,4), dtype = np.int32)
print(mx_1s)

mx_0s = np.zeros((4,6))
print(mx_0s)

mx_0s = np.zeros((4,6), dtype=bool)
print(mx_0s)

mx_0s = np.zeros((4,6),dtype = str)
print(mx_0s)

em_str = ''
print(bool(em_str))

em_mx = np.empty((3,3))
print(em_mx)