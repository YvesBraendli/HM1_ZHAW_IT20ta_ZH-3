import numpy as np
from BirrerBraendli_S8_Aufg2 import BirrerBraendli_S8_Aufg2
import timeit

# Aufgabe 2b

A = np.array([
    [1,-2,3],
    [-5,4,1],
    [2,-1,3]
])

Q,R = BirrerBraendli_S8_Aufg2(A)
print("Q:", Q)
print("R:", R)

# Aufgabe 2c

t1=timeit.repeat("BirrerBraendli_S8_Aufg2(A)","from __main__ import BirrerBraendli_S8_Aufg2, A", number=100)
t2=timeit.repeat("np.linalg.qr(A)","from __main__ import np, A", number=100)
avg_t1=np.average(t1)/100
avg_t2=np.average(t2)/100

print("AVG_t1:", avg_t1)
print("AVG_t2:", avg_t2)
print("Prozentualer Unterschied", ((avg_t2-avg_t1)/avg_t2))

# Aufgabe 2d

test = np.random.rand(100,100)

t1=timeit.repeat("BirrerBraendli_S8_Aufg2(test)","from __main__ import BirrerBraendli_S8_Aufg2, test", number=100)
t2=timeit.repeat("np.linalg.qr(test)","from __main__ import np, test", number=100)
avg_t1=np.average(t1)/100
avg_t2=np.average(t2)/100

print("AVG_t1:", avg_t1)
print("AVG_t2:", avg_t2)
print("Prozentualer Unterschied", ((avg_t2-avg_t1)/avg_t2))

'''
Die Linalg Funktion von Numpy ist schneller als unsere Funktion, dies für beide Durchführungen. Beim ersten Fall
ist es etwa doppelt so schnell beim zweiten Fall ist die numpy Funktion deutlich schneller nämlich bis zu 25 Mal schneller.
'''