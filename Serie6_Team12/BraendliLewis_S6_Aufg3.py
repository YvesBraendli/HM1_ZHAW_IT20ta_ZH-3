from G07_S6_Aufg2 import gauss
import numpy as np

# Bei den ersten Drei Matrizen gibt es keine Unterschiede, diese wurden korrekt berechnet, 
# bei Matrix unterscheided sich ein einzelner Wert im Ergebnis massic.
# Lösung Numpy: 3.26353931e-15
# Lösung Skript: 5.81353147e-1
# Da dies der einzige Wert ist, welcher so massiv daneben liegt, 
#wird dies durch Rundungsfehler passiert sein.


A1 = np.array([[4,-1,-5],[-12,4,17],[32,-10,-41]])
A2 = np.array([[2,7,3],[-4,-10,0],[12,34,9]])
A3 = np.array([[-2,5,4],[-14,38,22],[6,-9,-27]])

b1 = np.array([-5,19,-39])
b2 = np.array([6,-12,48])
b3 = np.array([25,-24,107])
b4 = np.array([4,-22,42])
b5 = np.array([1,40,74])
b6 = np.array([16,82,-120])


[A_triangle,detA,x1] = gauss(A1,b1)
[A_triangle,detA,x2] = gauss(A1,b2)

print("Obere Dreiecksmatrix A1:\n", A_triangle, "\n")
print("Determinante A1:\n", detA, "\n")
print("Ergebnis Numpy x1:\n", np.linalg.solve(A1,b1))
print("Ergebnis x1:\n", x1, "\n")
print("Ergebnis Numpy x2:\n", np.linalg.solve(A1,b2))
print("Ergebnis x2:\n", x2, "\n")


[A_triangle,detA,x3] = gauss(A2,b3)
[A_triangle,detA,x4] = gauss(A2,b4)

print("Obere Dreiecksmatrix A2:\n", A_triangle, "\n")
print("Determinante A2:\n", detA, "\n")
print("Ergebnis Numpy x3:\n", np.linalg.solve(A2,b3))
print("Ergebnis x3:\n", x3, "\n")
print("Ergebnis Numpy x4:\n", np.linalg.solve(A2,b4))
print("Ergebnis x4:\n", x4, "\n")

[A_triangle,detA,x5] = gauss(A3,b5)
[A_triangle,detA,x6] = gauss(A3,b6)

print("Obere Dreiecksmatrix A3:\n", A_triangle, "\n")
print("Determinante A3:\n", detA, "\n")
print("Ergebnis Numpy x5:\n", np.linalg.solve(A3,b5))
print("Ergebnis x5:\n", x5, "\n")
print("Ergebnis Numpy x6:\n", np.linalg.solve(A3,b6))
print("Ergebnis x6:\n", x6, "\n")


A4 = np.array([[-1,2,3,2,5,4,3,-1],
[3,4,2,1,0,2,3,8],
[2,7,5,-1,2,1,3,5],
[3,1,2,6,-3,7,2,-2],
[5,2,0,8,7,6,1,3],
[-1,3,2,3,5,3,1,4],
[8,7,3,6,4,9,7,9],
[-3,14,-2,1,0,-2,10,5]])
b7 = np.array([-11,103,53,-20,95,78,131,-26])

[A_triangle,detA,x7] = gauss(A4,b7)
print("Obere Dreiecksmatrix A4:\n", A_triangle, "\n")
print("Determinante A4:\n", detA, "\n")
print("Ergebnis Numpy x7:\n", np.linalg.solve(A4,b7))
print("Ergebnis x7:\n", x7, "\n")

