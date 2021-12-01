# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:30:31 2021

@author: yvesb
"""
import matplotlib.pyplot as plt
import numpy as np

#a)
# Es dauert jeweils bei jeder Infektionsrate eine gewisse Zeit, bis sich 
# genügend Kinder angesteckt haben, bis sich die Infektionszahlen
# stärker erhöhen (Initialphase). Anschliessend greift ein hoher a-Wert
# stärker und sorgt dafür, dass sich in einer kürzeren Zeit mehr Kinder anstecken.
# Ab einer Infektionsrate von ca. 2.5 werden die Werte wahllos und wir haben somit
# einen abstossenden Nullpunkt.
n=100
a=np.arange(0.1,4,0.1)
for ak in a:
    ki=0.1
    for k in range (n):
        ki=ak*ki*(1-ki)
        plt.scatter(ki,ak)
plt.xlim(0.5, 0.7)
plt.ylim(2, 3)
plt.grid()
plt.ylabel('Infektionsrate')
plt.xlabel('Anzahl infizierter Kinder %/100')

#b) Ein Fixpunkt hier würed bedeuten, dass sich keine Kinder mehr anstecken
# und gleichzeitig aber auch keine Kinder mehr genesen werden.

#val.append(ki)
#plt.scatter(ki,ak)
#plt.plot(val,valIt)
#print(val)
#print(valIt)
    