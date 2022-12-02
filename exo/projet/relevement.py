"""
@author: hiba doi
"""
from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=4, suppress=True)
nu=5
ROcc=636619.7724
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
    return round(xm,3),round(ym,3)


#fonction de différence
def delta(a,b):
    return b-a
#fonction de la distance
def d(X1,Y1,X2,Y2):
    return sqrt(delta(X1,X2)**2+delta(Y1,Y2)**2)
#fonction de gisement 
def Gt(X1,Y1,X2,Y2):
    deltax=delta(X1,X2)
   
    deltay=delta(Y1,Y2)
    
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
# paramètre d'homogination
ROcc=636619.7724
#les lectures horizontales
L=np.matrix([[0.0000],
            [71.8533],
            [142.5203],
            [199.4128],
            [206.1087],
            [340.4754]])
#les distance observées
D=np.matrix([[49.196],
            [46.935]])
#les coordonnées d'appuis angulaire
coo_app=np.matrix([[365793.69,377101.72],
                   [364824.43,375997.93],
                   [364767.96,373965.44],
                   [362154.53,374493.02],
                   [361977.97,375472.19],
                   [363236.12,377657.88]])
#coordonnées de point d'appuit linéaire
coo_app2=np.matrix([[364370.21,376076.10],
                    [364380.68,376131.72]])

X=[coo_app[0,0],coo_app[1,0],coo_app[2,0]]
Y=[coo_app[0,1],coo_app[1,1],coo_app[2,1]]
X0=np.matrix([rayonement(55.3290,129.5518-55.3290 , X, Y)])
#gisement  et distance des point des odservations angulaires
Gt_angulaire=[]
D_angulaire=[]

for i in range (6):
    Gt_angulaire.append([Gt(X0[0,0],X0[0,1],coo_app[i,0],coo_app[i,1])])
    D_angulaire.append([d(X0[0,0],X0[0,1],coo_app[i,0],coo_app[i,1])])
    
#gisement  et distance des point des odservations linaire

Gt_ln=[]
D_ln=[]

for i in range (2):
    Gt_ln.append([Gt(X0[0,0],X0[0,1],coo_app2[i,0],coo_app2[i,1])])
    D_ln.append([d(X0[0,0],X0[0,1],coo_app2[i,0],coo_app2[i,1])])
#V0 des observation angulaire

V0=[]
for i in range (6):
    alp=Gt_angulaire[i][0]
    l=L[i,0]
    V0.append(alp-l)
V0moyenne=round(mean(V0),5)

#WDij angulaire
WDij=[]

for i in range(6):
    WDij.append([V0[i]-V0moyenne])
#Wlij
WLij=[]

for i in range(2):
    x=D_ln[i][0]
    y=D[i,0]
    WLij.append([x-y])
A=[]
for i in range(6):
    A.append([-1,
              -ROcc*cosgr(Gt_angulaire[i][0])/D_angulaire[i][0],
              ROcc*singr(Gt_angulaire[i][0])/D_angulaire[i][0]])
for i in range(2):
    A.append([0,
              -singr(Gt_ln[i][0]),
              -cosgr(Gt_ln[i][0])])
XX0=[[V0moyenne]]
XX0.append([X0[0,0]])
XX0.append([X0[0,1]])
W=WDij+WLij


A=np.matrix(A)
B=-np.identity(8)



X00=np.matrix(XX0)
L=np.concatenate((L,D),axis=0)

P=np.identity(8)
I4=np.identity(8)
P_1=np.linalg.inv(P)
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)

A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
N_W=A_T*M_1*W
X=-1*N_1*N_W
Xes=X00+X
K=-M_1*(A*X+W)
V=P_1*B_T*K
Les=L+V
V_T=V.transpose()
sigma0_2=sigma0es=(V_T*P*V)/nu
sigma0_2=round(sigma0_2[0,0],5)
Cx=sigma0_2*N_1
Qk=M_1*(I4-A*(N_1)*A_T*M_1)
Ck=sigma0_2*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0_2*Qv
Ql=P_1-Qv
Cl=sigma0_2*Ql


    
