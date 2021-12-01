# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:08:06 2021

@author: yvesb
"""

def f(x):
     return (230*x**4+18*x**3+9*x**2-221*x-9)
 
def F(x):
     return (230*x**4+18*x**3+9*x**2-9)*(1/221)
tol = 10**(-6)
n = 0
x1 = -0.2
nmax = 5
while f(x1+tol)*f(x1-tol)>=0:
    x1=F(x1)
    n+=1
    if n>nmax:
        raise Exception('Keine Konvergenz vorhanden')
x2 = 0.9
m = 0 
nMax = 6  
while f(x2+tol)*f(x2-tol)>=0:
    x2=F(x2)
    m+=1
    if m>nMax:
        raise Exception('Keine Konvergenz vorhanden')
print(x1)
print(x2)
# Der Nullpunkt im Intervall [0,1] ist abstossend und der Nullpunkt im 
# Intervall [-1,0] anziehend. Man erreicht am Ende immer nur den Negativen Nullpunkt.
# Wenn der Startwert grösser als das Intervall gewählt wird, so kann die Iteration
# 6-Mal durchgeführt werden, bis ein OverflowError erscheint.