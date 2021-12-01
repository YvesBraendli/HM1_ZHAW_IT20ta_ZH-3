# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:58:58 2021

@author: yvesb
"""
import numpy as np

def gauss(A,b):
    A = np.array(A, dtype=np.float64)
    b=np.array(b, dtype=np.float64)
    n=A.shape[0]
    det=1
    if len(b)!=len(A):
        raise Exception('Anzahl Reihen im b Vektor ist ungleich der Anzahl Reihen in der Matrix A')
    count_line_swap=0
    for i in range(n):
        if A[i,i] ==0:
            l=-1
            for j in range(i+1, n):
                if A[j,i] !=0:
                    l=j
                    break
            if l==-1:
                raise Exception('Matrize singulär, keine Lösung vorhanden')
            #Zeilen tauschen
            A[[i,l],:] = A[[l,i],:]
            b[[i,l]] = b[[l,i]]
            #Eliminationsschritt
        for j in range(i+1,n):
            lam = A[j,i]/A[i,i]
            for e in range(n):
                A[j][e] = A[j][e]  - lam*A[i][e]
            b[j] = b[j] - lam*b[i]
        
        det *= A[i][i]
                #ev. besser: i+1: d.h. A[i,i+1:]
                #b ebenso
                #...
    # Rückwärtseinsetzen
    x = np.zeros_like(b)
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = b[i]
        for j in range(i+1,n):
            x[i] -= A[i][j]*x[j]
        x[i] = x[i]/A[i][i]
        
    

            
    return A, det, x
