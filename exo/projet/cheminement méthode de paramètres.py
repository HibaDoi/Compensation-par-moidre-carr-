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
    #print("deltax",deltax)
    deltay=delta(Y1,Y2)
    #print("deltay",deltay)
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
#paramètre d'homoginisation
R0cc=(200/pi)*10000
#sin et cos en grade
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)




#On va faire une fonction de calcul de cheminement par variation de paramètre

XD=[364227.83 ,376274.66]
XA=[364320.026 , 376378.770]
XRD=[364182.270 , 376218.180]
XRA=[364284.13 , 376312.34]
angle=[240.5711,123.5289,258.2405,365.9734]
distance=[45.56,68.92,46.91]

def CheminementP(XD,XA,XRD,XRA,angle,distance):
    Gd=Gt(XRD[0],XRD[1],XD[0],XD[1])
    #print(Gd)
    Ga=Gt(XA[0],XA[1],XRA[0],XRA[1])
    print(Ga)
    alphaij=[Gd]
    for i in range(len(angle)):
        alphaij.append(rp(alphaij[i]+angle[i]+200))
    
    
    co_APP=[[XD[0],XD[1]]]
    #a reviser dernier point
    for i in range(len(angle)-2):
        co_APP.append([co_APP[i][0]+distance[i]*singr(alphaij[i+1]),
                       co_APP[i][1]+distance[i]*cosgr(alphaij[i+1])])
    co_APP.append([364355.59,375870.61])
    #print(co_APP)    
    alpha0ij=[Gd]
    D0=[]
    for i in range(len(angle)-1):
        D0.append(d(co_APP[i][0],co_APP[i][1],co_APP[i+1][0],co_APP[i+1][1]))
    
    for i in range(len(angle)-1):
        alpha0ij.append(Gt(co_APP[i][0],co_APP[i][1],co_APP[i+1][0],co_APP[i+1][1]))
    print(alpha0ij)
        
    A=[[singr(alpha0ij[1]),cosgr(alpha0ij[1])]+[0]*((len(angle)-2)*2-2)]
    s=list(range(len(angle)-3))
    ss=s[::-1]
    for i in range(1,len(angle)-2):
        A.append([0]*2*(s[i-1])+[-singr(alpha0ij[i+1]),-cosgr(alpha0ij[i+1]),singr(alpha0ij[i+1]),cosgr(alpha0ij[i+1])]+[0]*2*(ss[i-1]))
    A.append([0]*2*(len(angle)-3)+[-singr(alpha0ij[3]),-cosgr(alpha0ij[3])])
    #A=np.matrix(A)
    
    A.append([R0cc*cosgr(alpha0ij[1])/D0[0]*0.01,
              -R0cc*singr(alpha0ij[1])/D0[0]*0.01]
             +[0]*((len(angle)-2)*2-2))
             
    A.append([R0cc*(cosgr(alpha0ij[1]+200)/D0[0]*0.01-cosgr(alpha0ij[2])/D0[1]*0.01),
              R0cc*(-singr(alpha0ij[1]+200)/D0[0]*0.01+singr(alpha0ij[2])/D0[1]*0.01),
              R0cc*cosgr(alpha0ij[2])/D0[1]*0.01,
              -R0cc*singr(alpha0ij[2])/D0[1]*0.01])

             
    A.append([
              R0cc*cosgr(alpha0ij[2])/D0[1]*0.01,
              -R0cc*singr(alpha0ij[2])/D0[1]*0.01,
              R0cc*(cosgr(alpha0ij[2]+200)/D0[1]*0.01-cosgr(alpha0ij[3])/D0[2]*0.01),
                        -R0cc*(singr(alpha0ij[2]+200)/D0[1]*0.01+singr(alpha0ij[3])/D0[2]*0.01),])

    A.append([0]*((len(angle)-2)*2-2)+
             [-R0cc*cosgr(alpha0ij[3])/D0[2]*0.01,
          -R0cc*singr(alpha0ij[3])/D0[2]*0.01])
    A=np.matrix(A)
    co_APP=np.matrix(co_APP)
    print(co_APP)
    print(A)
    print(alphaij)
    print(alpha0ij)
    coorint=np.matrix( [[364277.5734] ,[375872.1239],[364297.8145 ],[375838.7878]])
    print(coorint)
    print(D0)
    W=[]
    for  i in range(len(D0)):
        W.append(D0[i]-distance[i])
    print(W)
    beta=[]
    for i in range(len(alphaij)-1):
        beta.append(rp(alphaij[i+1]-alphaij[i]+200))
    print (beta,angle)
    for i in range(len(beta)):
        W.append((beta[i]-angle[i]))
    print(W)
    x=1/25
    y=1/196
    sigmaL=np.matrix([
        [x,0,0,0,0,0,0],
        [0,x,0,0,0,0,0],
        [0,0,x,0,0,0,0],
        [0,0,0,y,0,0,0],
        [0,0,0,0,y,0,0],
        [0,0,0,0,0,y,0],
        [0,0,0,0,0,0,y]])
    P=196*sigmaL
    print(P)
    return(X)
    
    
CheminementP(XD, XA, XRD, XRA, angle, distance)
# j in range((len(angle)-2)*2):