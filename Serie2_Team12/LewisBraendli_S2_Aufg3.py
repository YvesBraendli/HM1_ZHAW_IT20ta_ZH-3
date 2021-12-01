import numpy as np
import matplotlib.pyplot as plt
#a) Ab einer grossen Flöchenanzahl bricht die Gesamtsumme
# der einzelnen Flächen zusammen und geht auf 0 zurück, dies
# weil dann die Werte von s^2 gegen Null gehen und somit die
# Wurzel aus 1 gezogen wird, was in einer Wurzel aus 0 resultiert.
#niter = 30
#u = np.zeros(30)
#x = np.zeros(30)
#s = 1
#n = 6
#for k in range(niter):
#    u[k] = n*s
#    n*=2
#    x[k] = n
#    s = np.sqrt(2-2*np.sqrt(1-(s**2/4)))
    
#plt.title('Summe der Seitenlänge 2n*S2n')
#plt.xlabel('Anzahl Flächen')
#plt.ylabel('Summe der Seitenlänge')
#plt.plot(x,u)
#plt.grid()

#b) Hier wird beobachtet, dass sich ein Rundungsfehler von einem
# Wert auch auf die nachfolgenden auswirkt. Die Werte der Seitenlänge
# der Dreiecke verändert sich so wenig, dass die Werte immer auf 
# denselben Wert gerundet werden.
niter = 30
u = np.zeros(30)
x = np.zeros(30)
s = 1
n = 6
for k in range(niter):
    u[k] = n*s
    n*=2
    x[k] = n
    s = np.sqrt(s**2/(2*(1+np.sqrt(1-(s**2/4)))))
    
plt.title('Summe der Seitenlänge 2n*S2n')
plt.xlabel('Anzahl Flächen')
plt.ylabel('Summe der Seitenlänge')
plt.plot(x,u)
plt.grid()