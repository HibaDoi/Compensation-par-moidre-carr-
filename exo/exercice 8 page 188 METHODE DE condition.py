
import numpy as np
B=np.matrix([[0,1,-1,1,0,1,0],
             [0,0,1,0,1,1,1],
             [1,0,0,-1,1,0,1],
             [1,1,0,0,0,0,0]])

W=np.matrix([[-0.8],[0.4],[-0.5],[-0.5]])*10**-2
P=np.identity(7)
L=np.matrix([[3.075],   
   [2.479] ,
   [0.160],
   [1.238],
   [1.082],
   [2.001],
   [2.324]])

P_1=np.linalg.inv(P)
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)
I4=np.identity(4)





K=-M_1*(W)
V=P_1*B_T*K
Les=L+V
sigma0_2=1
V_T=V.transpose()

I4=np.identity(4)
Qk=M_1
Qv=P_1*B_T*Qk*B*P_1

Ql=P_1-Qv
Cl=sigma0_2*Ql
sigma0es=(V_T*P*V)/4



