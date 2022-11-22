import numpy as np
A=np.matrix([[1,0],[0,1],[1,1],[1,0]])

B=-np.identity(4)

W=np.matrix([[0],[0],[-0.03],[-0.01]])
i=10**7

X0=np.matrix([[100.010],[200.050]])
L=np.matrix([[100.010],   
   [200.050] ,
   [300.090],
   [100.020]])
P=np.identity(4)
I4=np.identity(4)
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
sigma0es=(V_T*P*V)/2



