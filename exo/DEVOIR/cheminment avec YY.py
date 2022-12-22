# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:03:53 2022

@author: hiba
"""

from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=2,suppress=False)
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
"""XD=[364316.26,376379.65]
XA=[364395.40,376265.09]
XRD=[364284.13,376312.34]
XRA=[364360.35,376219.61]
angle=[331.7425,218.2284,171.1972,292.2729]
distance=[39.571,44.690,57.545]"""
XD=[364395.40,376265.09]
XA=[364319.88,376385.35]
XRD=[364360.35,376219.61]
XRA=[364227.83,376274.66]
angle=[124.6592,200.5101,192.8923,84.3018]
distance=[44.908,47.090,50.184]
#paramètre d'homoginisation
R0cc=(200/pi)*10000
#sin et cos en grade
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)

Gd=round(Gt(XRD[0],XRD[1],XD[0],XD[1]),4)
#print(Gd)
Ga=round(Gt(XA[0],XA[1],XRA[0],XRA[1]),4)

alphaij=[Gd]
for i in range(len(angle)-2):
    alphaij.append(round(rp(alphaij[i]+angle[i]+200),4))


co_APP=[[XD[0],XD[1]]]
#a reviser dernier point
for i in range(len(angle)-2):
    co_APP.append([round(co_APP[i][0]+distance[i]*singr(alphaij[i+1]),3),
                   round(co_APP[i][1]+distance[i]*cosgr(alphaij[i+1]),3)])
co_APP.append(XA)
co_APP.append(XRA)
#print(co_APP)    
alpha0ij=[round(Gd,4)]
D0=[]
for i in range(len(angle)-1):
    D0.append(round(d(co_APP[i][0],co_APP[i][1],co_APP[i+1][0],co_APP[i+1][1]),3))

for i in range(len(angle)):
    alpha0ij.append(round(Gt(co_APP[i][0],co_APP[i][1],co_APP[i+1][0],co_APP[i+1][1]),4))

    
A=[[singr(alpha0ij[1]),cosgr(alpha0ij[1])]+[0]*((len(angle)-2)*2-2)]
s=list(range(len(angle)-3))
ss=s[::-1]
for i in range(1,len(angle)-2):
    A.append([0]*2*(s[i-1])+[-singr(alpha0ij[i+1]),-cosgr(alpha0ij[i+1]),singr(alpha0ij[i+1]),cosgr(alpha0ij[i+1])]+[0]*2*(ss[i-1]))
A.append([0]*2*(len(angle)-3)+[-singr(alpha0ij[3]),-cosgr(alpha0ij[3])])
#A=np.matrix(A)

A.append([R0cc*cosgr(alpha0ij[1])/D0[0]*0.001,
          -R0cc*singr(alpha0ij[1])/D0[0]*0.001]
         +[0]*((len(angle)-2)*2-2))
         
A.append([R0cc*(cosgr(alpha0ij[1]+200)/D0[0]*0.001-cosgr(alpha0ij[2])/D0[1]*0.001),
          R0cc*(-singr(alpha0ij[1]+200)/D0[0]*0.001+singr(alpha0ij[2])/D0[1]*0.001),
          R0cc*cosgr(alpha0ij[2])/D0[1]*0.001,
          -R0cc*singr(alpha0ij[2])/D0[1]*0.001])

         
A.append([
          R0cc*cosgr(alpha0ij[2])/D0[1]*0.001,
          -R0cc*singr(alpha0ij[2])/D0[1]*0.001,
          R0cc*(cosgr(alpha0ij[2]+200)/D0[1]*0.001-cosgr(alpha0ij[3])/D0[2]*0.001),
                    R0cc*(-singr(alpha0ij[2]+200)/D0[1]*0.001+singr(alpha0ij[3])/D0[2]*0.001),])

A.append([0]*((len(angle)-2)*2-2)+
         [-R0cc*cosgr(alpha0ij[3])/D0[2]*0.001,
      -R0cc*singr(alpha0ij[3])/D0[2]*0.001])
A=np.matrix(A)
co_APP=np.matrix(co_APP)

coorint=np.matrix( [[364277.5734] ,[375872.1239],[364297.8145 ],[375838.7878]])

W=[]
for  i in range(len(D0)):
    W.append(round(D0[i]-distance[i],2)*10**3)

beta=[]
for i in range(len(alpha0ij)-1):
    beta.append(round(rp(alpha0ij[i+1]-alpha0ij[i]+200),4))

for i in range(len(beta)):
    W.append(round((beta[i]-angle[i]),4)*10**4)
W=np.matrix(W).transpose()
x=1/25
y=1/(14**2)
sigmaL=np.matrix([
    [x,0,0,0,0,0,0],
    [0,x,0,0,0,0,0],
    [0,0,x,0,0,0,0],
    [0,0,0,y,0,0,0],
    [0,0,0,0,y,0,0],
    [0,0,0,0,0,y,0],
    [0,0,0,0,0,0,y]])
P=14**2*sigmaL
B=-np.identity(7)
I3=np.identity(7)
P_1=np.linalg.inv(P)
B_T=B
M=B*P_1*B_T
M_1=np.linalg.inv(M)
A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
N_W=A_T*M_1*W
X=-1*N_1*N_W
Xes=np.matrix([co_APP[1,0],co_APP[1,1],co_APP[2,0],co_APP[2,1]])+X.transpose()*10**-3
K=-M_1*(A*X+W)
V=P_1*B_T*K
#Les=L+V
#sigma0_2=c
V_T=V.transpose()
 #sigma0es=int((V_T*P*V)/3)
sigma0es=14**2
Cx=sigma0es*N_1
Qk=M_1*(I3-A*(N_1)*A_T*M_1)
Ck=sigma0es*Qk
Qv=P_1*B_T*Qk*B*P_1
Qv=P_1-A*N_1*A_T
Cv=sigma0es*Qv
#Ql=P_1-Qv
CL=np.linalg.inv(sigmaL)
Cl=CL-Cv
