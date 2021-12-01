# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:43:20 2021

@author: yvesb
"""
import math

def sekanten(f,x0,x1,tol):
    iter=0
    itermax=30
    while f(x1+tol)*f(x1-tol)>=0:
        x2=x1-(((x1-x0)/(f(x1)-f(x0)))*f(x1))
        x0=x1
        x1=x2
        iter+=1
        if iter>itermax:
            raise Exception('Keine Konvergenz vorhanden')
    return x2


def h(y):
    return math.e**(y**2)+(1/y**3)-10

y0=-1
y1=-1.2
tole=10**(-4)
print('Nullpunktüberprüfung mit Aufgabe 1 ergibt folgenden Nullpunkt:')
print(sekanten(h,y0,y1,tole))