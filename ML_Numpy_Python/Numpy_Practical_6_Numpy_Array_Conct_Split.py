# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:39:48 2019

@author: Vivek Vishan
"""

import numpy as np


arr_1 = np.arange(1,17).reshape(4,4)
print(arr_1)

arr_2 = np.arange(17,33).reshape(4,4)
print(arr_2)


list1 = [2,4,6,7]
list2 = [1,8,3,5]

list1 + list2

arr_1 + arr_2

np.concatenate((arr_1,arr_2))

np.concatenate((arr_1,arr_2),axis = 1)


np.vstack((arr_1,arr_2))

np.hstack((arr_1,arr_2))


np.hstack((arr_1,arr_2,arr_1))

np.split(arr_1,2)

arr_1

list_1 = np.split(arr_1,2)
type(list_1)

list_1[0]

type(list_1[0])

np.split(arr_1,2,axis = 1)

d1 =np.array([4,7,1,3,9])

np.split(d1,[1,3])