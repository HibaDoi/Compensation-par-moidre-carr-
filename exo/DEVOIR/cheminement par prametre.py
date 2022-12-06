# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:03:53 2022

@author: hiba
"""

from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=4,suppress=True)
#fonction de différence
def delta(a,b):
    return b-a
#fonction de la distance
def d(X1,Y1,X2,Y2):
    return sqrt(delta(X1,X2)**2+delta(Y1,Y2)**2)
#fonction de gisement 
def Gt(X1,Y1,X2,Y2):
    deltax=delta(X1,X2)
    print("deltax",deltax)
    deltay=delta(Y1,Y2)
    print("deltay",deltay)
    if deltax>=0 and deltay>=0:
        return atan(deltax/deltay)*200/pi
    elif deltax>=0 and deltay<=0:
        return atan(abs(deltay/deltax))*200/pi+100
    elif deltax<=0 and deltay<=0:
        return atan(deltax/deltay)*200/pi+200
    elif deltax<=0 and deltay>=0:
        return atan(abs(deltay/deltax))*200/pi+300
#fonction de parametrage des angle
def rp(s):
    if s <0:
        s+=400
    elif s> 400:
        s-=400
    return s

ROcc=(200/pi)*10000
#sin et cos en grade
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)




#On va faire une fonction de calcul de cheminement par variation de paramètre

def CheminementP(XD,XA,XRD,XRA,angle,distance):
    Gd=Gt(XD[0],XD[1],XRD[0],XRD[1])
    Ga=Gt(XA[0],XA[1],XRA[0],XRA[1])
    alphaij=[Gd]
    for i in range(len(angle)):
        alphaij.append(alphaij[i]+angle[i]+200)
    
    co_APP=[XD[0],XD[1]]
    for i in range(len(angle)):
        co_APP.append([co_APP[i,0]+distance[i]*singr(alphaij[i]),co_APP[i,1]+distance[i]*cosgr(alphaij[i])])
        
    alpha0ij=[]
    for i in range(len(angle)):
        alpha0ij.append(Gt())
    