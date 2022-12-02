"""
@author: hiba doi
"""
from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=4)

def cotangr(x):
    return 1/tan(x*pi/200)

#les angles 
def rayonement(alpha,beta,X,Y):
    r=(Y[1]-Y[0])+(X[1]-X[0])*cotangr(alpha)
    s=(X[1]-X[0])-(Y[1]-Y[0])*cotangr(alpha)
    p=(X[2]-X[1])-(Y[1]-Y[2])*cotangr(beta)+ s
    q=(Y[2]-Y[1])+(X[1]-X[2])*cotangr(beta)+ r
    xm=X[1]+(r*p-s*q)*q/(p**2+q**2)
    ym=Y[1]-(r*p-s*q)*p/(p**2+q**2)
    return [round(xm,2),round(ym,2)]
X=[363236.1200,364951.7600,365793.0900]
Y=[377657.8800,377249.9400,377101.7200]
print(rayonement(68.30680, 100.47560-68.30680, X, Y))
print(364420.5108,376084.4988)