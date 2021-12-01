# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:23:54 2021

@author: yvesb
"""

import numpy as np


def poly(a,xMin,xMax):
    c=np.shape(a)
    if(len(c)!=1 or len(a)==0):
        raise Exception('Falsche Arrayform, Koeffizienten entweder nicht vorhanden oder Array mehrdimensional')
    x=np.arange(xMin,xMax,0.1)
    p=np.zeros(x.size)
    m=a.size
    for k in range(m):
        p+=a[-(k+1)]*x**k

   
        
    dp=np.zeros(x.size)
    for i in range(m):
        dp+=i*a[-(i+1)]*x**(i-1)
        
        
    pint=np.zeros(x.size)
    for z in range(m):
        pint+=(a[-(z+1)]*x**(z+1))/(z+1)

    return(x,p,dp,pint)