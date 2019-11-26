# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:25:04 2019

@author: Vivek Vishan
"""

import numpy as np
import matplotlib.pyplot as plt

np.sin(180)


np.sin(90)


np.cos(180)


np.tan(180)

x_sin = np.arange(0,3*np.pi,0.1)
print(x_sin)

y_sin = np.sin(x_sin)
print(y_sin)


plt.plot(x_sin, y_sin)

y_cos = np.cos(x_sin)
plt.plot(x_sin,y_cos)
plt.show()


y_tan = np.tan(x_sin)
plt.plot(x_sin,y_tan)
plt.show()

