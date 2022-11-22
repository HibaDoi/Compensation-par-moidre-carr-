from math import *
from statistics import mean
import numpy as np
nu=1
def delta(a,b):
    return b-a
def d(X1,Y1,X2,Y2):
    return sqrt(delta(X1,X2)**2+delta(Y1,Y2)**2)
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
def rp(s):
    if s <0:
        s+=400
    elif s> 400:
        s-=400
    return s
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)
ROcc=636619.7724
    
GT12=Gt(361635.14,371760.86,361683.49,371715.17)
GT17=Gt(361635.14,371760.86,361589.61,371732.01)
GT1B=GT17+277.2801-400
X=[361635.14,371760.86]
alpha=GT12-GT1B
alpha2=400-(277.2801+(GT17-GT12))
beta=65.423
phi=200-(alpha+beta)
d12=d(361635.14,371760.86,361683.49,371715.17)
b10=d12*sin(beta*pi/200)/sin(phi*pi/200)
Xb=X[0]+b10*sin(GT1B*pi/200)
Yb=X[1]+b10*cos(GT1B*pi/200)
b20=d(Xb,Yb,361683.49,371715.17)
GT2B=GT12-200+beta
GTB1=rp(GT1B-200)
GTB2=rp(GT2B-200)
V0m1=rp(GT1B-277.2801)
V021=348.1997
V02B=rp(13.6225-65.423)
V0m2=mean([V021,V02B])
W=[]
GT21=rp(GT12-200)
W.append((GT17-V0m1-0)*10**4)
W.append(rp(GT1B-V0m1-277.2801)*10**4)
W.append((GT21-V0m2-0)*10**4)
W.append((rp(GT2B-V0m2-65.423))*10**4)
Wdistance=b10-62.80
W.append(Wdistance*10**3)
W=np.matrix(W)
W=W.transpose()

A=np.matrix([[-1,0,0,0],
            [-1,0,ROcc*cosgr(GT1B)/b10*10-3,-ROcc*singr(GT1B)/b10*10-3],
            [0,-1,0,0],
            [0,-1,ROcc*cosgr(GT2B)/b20*10-3,-ROcc*singr(GT2B)/b20*10-3],
            [0,0,singr(GT1B)*ROcc,cosgr(GT1B)*ROcc]])

Cl=np.matrix([[400,0,0,0,0],
    [0,400,0,0,0],
    [0,0,400,0,0],
    [0,0,0,400,0],
    [0,0,0,0,400]])
P=400*np.linalg.inv(Cl)

B=-np.identity(5)
P_1=np.linalg.inv(P)
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)

A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
N_W=A_T*M_1*W
X=-1*N_1*N_W
X0=np.matrix([0,0,Xb,Yb])
X0=X0.transpose()

Xes=X0+X
L=np.matrix([[0],
             [287.2801],
             [0],
             [65.4230],
             [62.80]])
I5=np.identity(5)
K=-M_1*(A*X+W)
V=P_1*B_T*K
Les=L+V
sigma0_2=(0.05)**2
Cx=sigma0_2*N_1
Qk=M_1*(I5-A*(N_1)*A_T*M_1)
Ck=sigma0_2*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0_2*Qv
Ql=P_1-Qv
Cl=sigma0_2*Ql
V_T=V.transpose()
sigma0es=(V_T*P*V)/1
test=A_T*P*V
rapport_chi_carré=nu*sigma0es/3.84