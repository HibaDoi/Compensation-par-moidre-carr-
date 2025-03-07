from math import *
import numpy as np
np.set_printoptions(precision=3, suppress=True)
nu=11
#Matrice A
A=np.matrix([[0.0016],[0.0016],[0.0016],[0.0016],[0.00225],[0.00225],[0.00225],[0.00225],[1],[1],[1],[1]])
#Matrice B est égale a la négation
B=-np.identity(12)
W=np.matrix([[0.1329],[-0.6671],[-0.2671],[0.3329],[-0.315],[0.285],[-0.215],[0.015],[0],[-126],[-49],[-131]])
a=b=(0.05)**2
c=50**2
CL=np.matrix([[a,0,0,0,0,0,0,0,0,0,0,0],
              [0,a,0,0,0,0,0,0,0,0,0,0],
              [0,0,a,0,0,0,0,0,0,0,0,0],
              [0,0,0,a,0,0,0,0,0,0,0,0],
              [0,0,0,0,b,0,0,0,0,0,0,0],
              [0,0,0,0,0,b,0,0,0,0,0,0],
              [0,0,0,0,0,0,b,0,0,0,0,0],
              [0,0,0,0,0,0,0,b,0,0,0,0],
              [0,0,0,0,0,0,0,0,c,0,0,0],
              [0,0,0,0,0,0,0,0,0,c,0,0],
              [0,0,0,0,0,0,0,0,0,0,c,0],
              [0,0,0,0,0,0,0,0,0,0,0,c]
              ])
sigma0=c
P=sigma0*np.linalg.inv(CL)

S0=np.matrix([[31311]])
L=[[99.7],[100.5],[100.1],[99.5],[141.5],[140.9],[141.4],[141.2],[31311],[31437],[31360],[31442]]
B=-np.identity(12)
I3=np.identity(12)
P_1=np.linalg.inv(P)
B_T=B
M=B*P_1*B_T
M_1=np.linalg.inv(M)
A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
N_W=A_T*M_1*W
X=-1*N_1*N_W
Ses=S0+X
K=-M_1*(A*X+W)
V=P_1*B_T*K
Les=L+V
sigma0_2=c
V_T=V.transpose()
sigma0es=int((V_T*P*V)/nu)
Cx=sigma0es*N_1
Qk=M_1*(I3-A*(N_1)*A_T*M_1)
Ck=sigma0es*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0es*Qv
#Ql=P_1-Qv
Cl=CL-Cv






