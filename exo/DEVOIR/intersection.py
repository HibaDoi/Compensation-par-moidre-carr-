"""
@author: hiba doi
"""
from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=4)
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
#sin et cos en grade
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)


def intersection(alpha,beta,X,Y):
    D12=d(X[0],Y[0],X[1],Y[1])
    GT12=rp(Gt(X[0],Y[0],X[1],Y[1]))
    GT21=rp(Gt(X[0],Y[0],X[1],Y[1])+200)
    GT1M=rp(GT12+alpha)
    D1M=singr(beta)*D12/singr(200-bata-alpha)
    xm=X[0]+D1M*singr(GT12)
    ym=Y[0]+D1M*cosgr(GT12)
    return xm,ym
    