# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:33:24 2021

@author: yvesb
"""

import matplotlib.pyplot as plt
import numpy as np
#a)
# Das geschieht, weil der Wert unter der Wurzel mit 1.1 0 ergibt.
# Wurzel aus Null nicht berechenbar. Wenn der Wert nahe genug kommt,
# wird er von der Maschinengenauigkeit als Null berechnet und ergibt somit
# keine unendliche Genauigkeit.

#x = np.arange(0,2,0.1)
#y = ((100*x**2)-200*x+99)**(1/2)
#plt.plot(x,y)
#plt.xlim(0, 2.5)
#plt.ylim(-0.5, 3)
#plt.grid()
#plt.xlabel('x-Achse')
#plt.ylabel('y-Achse')
#plt.title('Funktionsgraph der Aufgabe eins inkl. Ableitungs- und Stammfunktionsgraphen')
#plt.legend(['Funktion', 'Ableitung', 'Stammfunktion'])

#b)
x = np.arange(1.1,1.3, 10**(-7))
yOrigin = ((100*x**2)-200*x+99)**(1/2)
yDerived = ((100*x-100)/((100*x**2)-200*x+99)**(1/2))
y = abs((yDerived/yOrigin)*x)
print(y)
plt.plot(x,y)
plt.xlim(1.05, 1.35)
plt.ylim(4.5, 10)
plt.grid()
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Funktionsgraph der Aufgabe eins inkl. Ableitungs- und Stammfunktionsgraphen')
plt.legend(['Funktion', 'Ableitung', 'Stammfunktion'])

# c)
# Die Auslöschung kann nicht verhindert werden, da die Funktion eine schlechte 
# Kondition aufweist (ca. 4.875 und steigend)