# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:03:53 2022

@author: FY
"""

from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=9,suppress=False)
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


def intersection(alpha,beta,X,Y):
    D12=d(X[0],Y[0],X[1],Y[1])
    GT12=rp(Gt(X[0],Y[0],X[1],Y[1]))
    GT21=rp(Gt(X[0],Y[0],X[1],Y[1])+200)
    GT1M=rp(GT12+alpha)
    D1M=singr(beta)*D12/singr(200-beta-alpha)
    xm=X[0]+D1M*singr(GT1M)
    ym=Y[0]+D1M*cosgr(GT1M)
    return xm,ym

'Coordonnees des points '
topo12=[ 364229.83 , 376274.66]
Park2=[364286.7500 , 376286.6200]
Park3=[364284.1300 , 376312.3400]
"Calcul des coord approchées "
X=[364229.0000,364286.7500 ]
Y=[376274.0000,376286.6200]
alpha=55.08495
beta=400-340.65430
[xm0,ym0]=intersection(alpha, beta, X, Y)


M=[xm0,ym0]
'Calcul des Gisements des direction alpha ij '
L=[0,25.2134,80.2984,0,340.65430,0,353.81075]
alphaij=[]
alphaij.append(Gt(topo12[0],topo12[1],Park3[0],Park3[1]))
alphaij.append(Gt(topo12[0],topo12[1],Park2[0],Park2[1]))
alphaij.append(Gt(topo12[0],topo12[1],M[0],M[1]))

alphaij.append(Gt(Park2[0],Park2[1],topo12[0],topo12[1]))
alphaij.append(Gt(Park2[0],Park2[1],M[0],M[1]))


alphaij.append(Gt(Park3[0],Park3[1],topo12[0],topo12[1]))
alphaij.append(Gt(Park3[0],Park3[1],M[0],M[1]))
'Calcul des distances approchées'
lij=[]
lij.append(d(topo12[0],topo12[1],Park3[0],Park3[1]))
lij.append(d(topo12[0],topo12[1],Park2[0],Park2[1]))
lij.append(d(topo12[0],topo12[1],M[0],M[1]))

lij.append(d(Park2[0],Park2[1],topo12[0],topo12[1]))
lij.append(d(Park2[0],Park2[1],M[0],M[1]))


lij.append(d(Park3[0],Park3[1],topo12[0],topo12[1]))
lij.append(d(Park3[0],Park3[1],M[0],M[1]))
"Calcul de la constante d orientation Goi et Gom"
V0=[]
for i in range(7) :
    V0.append(rp(alphaij[i]-L[i]))

V0m=[mean([V0[0],V0[2]]),mean([V0[0],V0[2]]),mean([V0[0],V0[2]])
     ,mean([V0[3],V0[4]]),mean([V0[3],V0[4]]),
  mean([V0[5],V0[6]]),mean([V0[5],V0[6]])]

'Calcul des directions approchés et de W (en grade) '
W=[]
for i in range(7) :
    W.append(alphaij[i]-V0m[i]-L[i])
W[4]+=400
W[6]+=400


W=np.matrix([W])
W=W.transpose()
'Calcul de A'
A=np.matrix([[-1,0,0,0,0],
            [-1,0,0,0,0],
            [-1,0,0,(-ROcc*cosgr(alphaij[2])/lij[2]),(ROcc*singr(alphaij[2])/lij[2])],
            [0,-1,0,0,0],
            [0,-1,0,(-ROcc*cosgr(alphaij[4])/lij[4]),(ROcc*singr(alphaij[4])/lij[4])],
            [0,0,-1,0,0],
            [0,0,-1,(-ROcc*cosgr(alphaij[6])/lij[6]),(ROcc*singr(alphaij[6])/lij[6])]]
           )
"X0 APPROCHEE"
X0=[V0m[1],V0m[3],V0m[6],M[0],M[1]]
X0=np.matrix([X0])
X0=X0.transpose()
"Calcul des matrice et des X^ et des X corrigés"
P=np.identity(7)
P_1=np.linalg.inv(P)
M=P_1
M_1=np.linalg.inv(M)
A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
U=A_T*M_1*W
hX=-1*N_1*U
Xes=X0+hX
'Correction des observations (en grade)'
V=A*hX+W
V_T=V.transpose()
K=-M_1*(A*hX+W)
L=np.matrix([L])
L=L.transpose()
Les=L+V
'pas de sigma0_2 dans l enoncé on va prend  7cc'
sigma0_2=900
sigma0es=(V_T*P*V)/3
sigmaX=sigma0_2*N_1
Qk=M_1*(P-A*(N_1)*A_T*M_1)
sigmaK=sigma0_2*Qk
Qv=P_1*(-P)*Qk*P*P_1
sigmaV=sigma0_2*Qv
Ql=P_1-Qv
sigmaL=sigma0_2*Ql
'X est en cc et m puisqu on a travaillé avec des distances en m , et c est pareil pour les sigmas VarCov'
