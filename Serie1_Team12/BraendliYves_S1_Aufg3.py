# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:19:23 2021

@author: yvesb
"""
import numpy as np
import timeit

def fact_for(n):
    x = 1
    numbers = list(range(1,n+1,1))
    for i in numbers:
        x = x*i
    return x

def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)
    

t1 = timeit.repeat("fact_rec(500)","from __main__ import fact_rec", number=100)
t2 = timeit.repeat("fact_for(500)","from __main__ import fact_for", number=100)
timeone=0
for i in t1:
    timeone = timeone+i
timeone/5
timetwo=0
for i in t2:
    timetwo = timetwo+i
timetwo/5
print(timeone/timetwo)
# Die Funktion mit der for-Schleife ist schneller und das um ca. einen Faktor
#zwischen 8.5 und 9.5.
# Dies weil er die rekursive Funktion immer wieder aufrufen muss und immer
# ein Zwischenresultat speichern muss. Bei der for-Schleife muss er nicht
# eine ganze Funktion, sondern nur ein Schleife repetitiv aufrufen.

#Als Integer funktionieren beide Ausdrücke und es werden sehr grosse Zahlen
#zurückgegeben, welche aufgrund von ihrer Grösse nicht überprüpft werden können.
#Als float erhält man eine RuntimeWarning, weil es einen overflow in
#double_scalars gegeben hat.