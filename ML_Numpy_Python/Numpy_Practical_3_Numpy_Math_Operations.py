# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:45:08 2019

@author: Vivek Vishan
"""

import numpy as np
 
arr_1 = np.arange(1,10).reshape(3,3)
arr_2 = np.arange(1,10).reshape(3,3)
print(arr_1)
print(arr_2)


# addition
arr_1 + arr_2

np.add(arr_1, arr_2)

#Subtraction
arr_1 - arr_2

np.subtract(arr_1, arr_2)

#Division

arr_1 / arr_2

np.divide(arr_1, arr_2)


#Multiplication

arr_1 * arr_2

np.multiply(arr_1, arr_2)

#Element wise multiuplication
arr_1 @ arr_2

#dot product
arr_1.dot(arr_2)

arr_1

#Max Value
arr_1.max()

#index of min or max value
arr_1.argmax()


#row or col max value
arr_1.max(axis=0)

arr_1.max(axis=1)


#Max Value
arr_1.min()

#index of min or max value
arr_1.argmin()

#row or col max value
arr_1.min(axis=0)

arr_1.min(axis=1)

arr_1

#Sum Function
np.sum(arr_1)

#Row wise Sum
np.sum(arr_1, axis=1)

#Col wise Sum
np.sum(arr_1, axis=0)

#Average Function
np.mean(arr_1)

#square root
np.sqrt(arr_1)

#Standard deviation
np.std(arr_1)

#Expontional Fun
np.exp(arr_1)

#Log function
np.log(arr_1)

np.log10(arr_1)