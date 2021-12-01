import numpy as np
import matplotlib.pyplot as plt
from LewisBraendli_S6_Aufg2 import gauss

# Aufgabe 3a

'''
Polynom dritten Grades: y = x**3+x**2+x**1+x**0
x-Werte: 0,2,9,13
Gleichung:
a*(0)**3+b*(0)**2+c*(0)**1+d*(0)**0=150
a*(2)**3+b*(2)**2+c*(2)**1+d*(2)**0=104
a*(9)**3+b*(9)**2+c*(9)**1+d*(9)**0=172
a*(13)**3+b*(13)**2+c*(13)**1+d*(13)**0=152
'''

in1 = np.array([0,2.,9.,13.])

A1 = np.array([
    [in1[0]**3,in1[0]**2,in1[0]**1,in1[0]**0],
    [in1[1]**3,in1[1]**2,in1[1]**1,in1[1]**0],
    [in1[2]**3,in1[2]**2,in1[2]**1,in1[2]**0],
    [in1[3]**3,in1[3]**2,in1[3]**1,in1[3]**0],
])

b = np.array([150.,104.,172.,152.])

results = gauss(A1,b)[2]


def f1(x):
    return results[0]*x**3 + results[1]*x**2 + results[2]*x + results[3]

x_values = np.arange(1997,2010,0.1)
plt.plot(x_values,f1(x_values-1997))
plt.plot(1997, 150, 'r+')
plt.plot(1999, 104, 'r+')
plt.plot(2006, 172, 'r+')
plt.plot(2010, 152, 'r+')
plt.grid()
plt.show()

# Aufgabe 3b
print("Schätzungswert für 2003:", f1(6))
print("Schätzungswert für 2004:", f1(7))


# Aufgabe 3c

x = np.array([0.0,2.0,9.0,13.0])
y = np.array([150.0,104.0,172.0,152.0])
z = np.polyfit(x,y,3)
print("Koeffizienten errechnet durch Funktion: \n",z)
print("Koeffizienten errechnet durch Gauss: \n", results)

def f2(x):
    return np.polyval([z[0],z[1],z[2],z[3]],x)

plt.plot(x_values,f2(x_values-1997))
plt.grid()
plt.show()
