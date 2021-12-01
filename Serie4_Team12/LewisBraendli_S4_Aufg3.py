# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:35:03 2021

@author: yvesb
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-10,10,0.1)
u = np.zeros(len(x))
xSin=[]
niter = 0
for k in x:
    u[niter] = math.sin(k)
    niter +=1
f = ((2*(u-x))/math.pi)+1

F = ((1/2)*math.pi)+u

plt.plot(x,f)
plt.plot(x, F)
plt.xlim(-2, 3)
plt.ylim(-1, 5)
plt.grid()
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Funktionsgraphen f(x) und F(x)')
plt.legend(['f(x)', 'F(x)'])

x0=2
for k in range(30):
    x0=((1/2)*math.pi)+math.sin(x0)
    print(round(x0,4))
#b) Der Nullpunkt konvergiert gegen 2.3099 bei einer Genauigkeit von 10^-3