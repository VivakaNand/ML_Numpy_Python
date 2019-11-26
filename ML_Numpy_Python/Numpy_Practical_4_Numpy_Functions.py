# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:30:40 2019

@author: Vivek Vishan
"""

#Numpy Functions
import numpy as np

#arange()
#np.arange(start, end, steps)
arr_1d = np.arange(1,13)
print(arr_1d)


even_arr = np.arange(0,13,2)
print(even_arr)

#linspace()
lin_sp = np.linspace(1,5,4)
print(lin_sp)


#reshape()
arr_2d = arr_1d.reshape(2,6)
print(arr_2d)


arr_2d = arr_1d.reshape(3,4)
print(arr_2d)


arr_3d = arr_1d.reshape(2,3,2)
print(arr_3d)


arr = np.arange(1,13).reshape(2,6)
print(arr)

#ravel()
arr.ravel() 


#flatten()
arr.flatten()

#transpose()
arr.transpose()

arr.T