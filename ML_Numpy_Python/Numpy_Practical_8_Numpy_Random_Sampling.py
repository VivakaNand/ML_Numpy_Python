# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:34:25 2019

@author: Vivek Vishan
"""

import numpy as np
import random


np.random.random(1)

np.random.random((3,3))

np.random.randint(1,4)


np.random.randint(1,4,(4,4))



np.random.randint(1,4,(2,4,4))

np.random.seed(10)
np.random.randint(1,4,(2,4,4))


np.random.seed(10)
np.random.randint(1,4,(2,4,4))


2**32 -1


np.random.rand(3)


np.random.rand(3,3)


x = [1,2,3,4]
np.random.choice(x)


x = [1,2,3,4]
np.random.choice(x)



x = [1,2,3,4]
np.random.choice(x)

for i in range(20):
    print(np.random.choice(x))
    
    
x

np.random.permutation(x)



np.random.permutation(x)