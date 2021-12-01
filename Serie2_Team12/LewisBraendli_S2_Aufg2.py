import numpy as np
import matplotlib.pyplot as plt
#a) Bei f1 wird jedes Element einzeln gerechnet und somit mit einem "verfälschten"
# Wert weitergerechnet. Das Ergebnis sieht man in den Ausschlägen in f1.
# Ein weiteres Element hier ist, dass die Reihenfolge der Additionen nicht
# sortiert ist und sich somit Rundungsfehler einschleichen, da wahllos
# grosse und kleine Werte nacheinander addiert werden
#a= 1.99
#b = 2.01
#distance = (b-a)/501

#x = np.arange(a,b,distance)
#f1 = x**7 -14*x**6+84*x**5-280*x**4+560*x**3-672*x**2+448*x-128
#f2 = (x-2)**7

#plt.plot(x,f1)
#plt.plot(x,f2)
#plt.legend(['polynom f1', 'polynom f2'])
#plt.xlim(a,b)
#plt.title('Polynome f1 und f2')
#plt.xlabel('x-Achse')
#plt.ylabel('y-Achse')
#plt.grid()

#b) Sie ist nicht stabil, da sich die beiden Werte im Nenner aufgrund ihrer
# Nähe gegenseitig auslöschen.
#a = 1*-10**-14
#b = 10**(-14)
#c = 10**(-17)
#xNeg = np.arange(a, 0, c)
#xPos = np.arange(0, b, c)
#gNeg = xNeg/(np.sin(1+xNeg)-np.sin(1))
#gPos = xPos/(np.sin(1+xPos)-np.sin(1))

#plt.plot(xPos, gPos)
#plt.plot(xNeg, gNeg)
#plt.legend(['Positiv', 'Negativ'])
#plt.title(['Grenzwert-Plot'])
#plt.xlabel('x-Achse')
#plt.ylabel('y-Achse')
#plt.grid()

#c) Die Werte gehen stabiler gegen unendlich.
a = 1*-10**-14
b = 10**(-14)
c = 10**(-17)
xNeg = np.arange(a, 0, c)
xPos = np.arange(0, b, c)
gNeg = xNeg/(np.sin(2*np.cos((1+xNeg+1)/2)*np.sin((1+xNeg-1)/2)))
gPos = xPos/(np.sin(2*np.cos((1+xPos+1)/2)*np.sin((1+xPos-1)/2)))

plt.plot(xPos, gPos)
plt.plot(xNeg, gNeg)
plt.legend(['Positiv', 'Negativ'])
plt.title(['Grenzwert-Plot'])
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.grid()
