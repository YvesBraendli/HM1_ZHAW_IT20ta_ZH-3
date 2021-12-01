# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:33:24 2021

@author: yvesb
"""

import matplotlib.pyplot as plt
import numpy as np
import math

xf = np.arange(0,100,1.1)
yf = 5/((2*xf**2)**(1/3))


plt.subplot(3, 1, 1)
plt.plot(xf,yf)
plt.semilogy()
plt.semilogx()
plt.xlim(-100, 1000)
plt.ylim(-100, -100)
plt.grid()
plt.ylabel('y-Achse')
plt.legend(['Funktion f(x)'])

xg = np.arange(0,100,1)
yg = 10**5*(2*math.e)**(-xg/100)

plt.subplot(3, 1, 2)
plt.plot(xg,yg)
plt.semilogy()
plt.xlim(-10, 100)
plt.ylim(-100, -100)
plt.grid()
plt.ylabel('y-Achse')
plt.legend(['Funktion g(x)'])

xh = np.arange(0,100,1)
yh = ((10**(2*xh))/(2**(5*xh)))**2


plt.subplot(3, 1, 3)
plt.plot(xh,yh)
plt.semilogy()
plt.xlim(0, 4)
plt.ylim(-100, -100)
plt.grid()
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.legend(['Funktion h(x)'])

plt.show()