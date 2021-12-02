# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:32:36 2021

@author: yvesb
"""

import numpy as np
import time
import matplotlib.pyplot as plt
from Team12_S10_Aufg3a import Team12_S10_Aufg3a
#from Team12_S6_Aufg2 import gauss


# Aufgabe 3b

dim  = 3000
A    = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))
dum1 = np.arange(1,np.int(dim/2+1),dtype=np.float64).reshape((np.int(dim/2),1))
dum2 = np.arange(np.int(dim/2),0,-1,dtype=np.float64).reshape((np.int(dim/2),1))
x    = np.append(dum1,dum2,axis=0)
b    = A@x
x0   = np.zeros((dim,1))
tol  = 1e-4

start = time.time()
x1,n,n2 = Team12_S10_Aufg3a(A,b,x0,tol,1)
stop = time.time()

t1 = stop-start

start = time.time()
x2,n,n2 = Team12_S10_Aufg3a(A,b,x0,tol,2)
stop = time.time()

t2 = stop-start

start = time.time()
#x3=gauss(A,b)
x3 = np.linalg.solve(A,b)
stop = time.time()

t3 = stop-start

print('Zeit Jacobi-Verfahren:', t1)
print('Zeit Gauss-Seidel-Verfahren:', t2)
print('Zeit Gauss-Verfahren:', t3)

x1_fehler = np.subtract(x3.reshape(dim,1),x1)
x2_fehler = np.subtract(x3.reshape(dim,1),x2)
x3_fehler = np.subtract(x3.reshape(dim,1),x3)

plt.plot(x1_fehler,color='blue',label='Fehler Jacobi-Verfahren')
plt.plot(x2_fehler,color='red',label='Fehler Gauss-Seidel-Verfahren')
plt.plot(x3_fehler,color='yellow',label='Fehler Gauss-Verfahren')
plt.xlabel("Elemente des Lösungsvektors")
plt.legend()


'''
Leider konnten wir das Resultat für die 3000x3000 Matrix nicht mit unserer Funktion aus der Serie 6 in einer
angemessenen Zeit berechnen (wir haben ca. 1h gewartet). Daher haben wir nur mit einer 300x300 Matrix gerechnet
und sind zum Schluss gekommen, dass das Gaus-Seidel-Verfahren ca. eine Grössenordnung genauer ist als das Jacobi-Verfahren.
'''