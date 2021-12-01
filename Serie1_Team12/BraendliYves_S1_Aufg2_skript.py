# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:41:13 2021

@author: yvesb
"""
import numpy as np
import matplotlib.pyplot as plt
from BraendliYves_S1_Aufg2 import poly
[x,p,dp,pint] = poly(np.array([1,-5, -30, 110, 29, -105]), -10, 10)

plt.plot(x, p)
plt.plot(x, dp)
plt.plot(x, pint)
plt.xlim(-10, 10)
plt.ylim(-2800, 2800)
plt.grid()
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Funktionsgraph der Aufgabe eins und zwei \n inkl. Ableitungs- und Stammfunktionsgraphen')
plt.legend(['Funktion', 'Ableitung', 'Stammfunktion'])
