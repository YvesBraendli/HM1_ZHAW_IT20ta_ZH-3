
#Binär
epsBi = 1
while epsBi+1 > 1:
    epsBi /= 2
epsBi *=2
#epsBi += 1
print(epsBi)

#Dezimal
epsDez = 5
while epsDez+1 >1:
    epsDez /= 10
epsDez *= 10
print(epsDez)

#Der Rechner arbeitet im Dualsystem, da dort eps viel kleiner ist.

#QMax

qmax = 1.0
while qmax+1.0 > qmax:
    qmax *=2
qmax/=2
print(qmax)
#qMax lässt sich nicht direkt aus epsBi berechnen.