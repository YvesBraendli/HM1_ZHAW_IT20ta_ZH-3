# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:33:24 2021

@author: yvesb
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10,0.1)
yOrigin = x**5-5*x**4-30*x**3+110*x**2+29*x-105

yDerived = 5*x**4-20*x**3-90*x**2+220*x+29

yAntiderivative = ((x-2)*x*(x**4-4*x**3-53*x**2+114*x+315))/6

plt.plot(x,yOrigin)
plt.plot(x, yDerived)
plt.plot(x, yAntiderivative)
plt.xlim(-10, 10)
plt.ylim(-2800, 2800)
plt.grid()
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Funktionsgraph der Aufgabe eins inkl. Ableitungs- und Stammfunktionsgraphen')
plt.legend(['Funktion', 'Ableitung', 'Stammfunktion'])