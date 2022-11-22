import numpy as np
from math import *
A=np.matrix([[1,0,0],
             [-1,0,0],
             [-1,0,1],
             [0,-1,1],
             [1,-1,0],
             [0,1,0],
             [0,0,-1]])
L=np.matrix([[3.075],   
   [2.479] ,
   [0.160],
   [1.238],
   [1.082],
   [2.001],
   [2.324]])
X0=np.matrix([[97.777],[96.703],[97.937]])
WW=A*X0-L+[[-94.704],
          [100.261],
          [0],
          [0],
          [0],
          [-94.704],
          [100.261]]
W=np.matrix([[0],[0.5],[0],[-0.4],[-0.8],[0],[0]])*10**-2


B=-np.identity(7)


i=10**7



P=np.identity(7)
I4=np.identity(7)
P_1=np.linalg.inv(P)
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)

A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
N_W=A_T*M_1*W
X=-1*N_1*N_W
Xes=X0+X
K=-M_1*(A*X+W)
V=P_1*B_T*K
Les=L+V
sigma0_2=(0.05)**2
Cx=sigma0_2*N_1
Qk=M_1*(I4-A*(N_1)*A_T*M_1)
Ck=sigma0_2*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0_2*Qv
Ql=P_1-Qv
Cl=sigma0_2*Ql
V_T=V.transpose()
sigma0es=(V_T*P*V)/4
print(sqrt(7.5e-06))




