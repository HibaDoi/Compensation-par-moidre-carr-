
import numpy as np
A=np.matrix([[1,0,0],
             [0,1,0],
             [0,0,1],
             [0,1,1],
             [1,1,0],
             [1,1,1]])

B=-np.identity(6)

W=np.matrix([[0],
             [0],
             [0],
             [-7],
             [2],
             [1]])
i=10**7

X0=np.matrix([[200.04],[200.01],[199.92]])
L=np.matrix([[200.04],   
             [200.01] ,
             [199.98],
             [400.00],
             [400.02],
             [599.96]])
P=np.identity(6)
I6=np.identity(6)
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
Qk=M_1*(I6-A*(N_1)*A_T*M_1)
Ck=sigma0_2*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0_2*Qv
Ql=P_1-Qv
Cl=sigma0_2*Ql
V_T=V.transpose()
sigma0es=(V_T*P*V)/3
C=np.matrix([[0,1,0],
   [0,0,1]])
Wc=np.matrix([[6],[-2]])
C_T=C.transpose()
D=(C*N_1*C_T)
D_1=np.linalg.inv(D)
Xc=X+N_1*C_T*(D_1)*(-Wc+C*N_1*N_W)
Kc=-M_1*(A*Xc+W)
Vc=P_1*B_T*Kc
sima0ces=(V_T*P*V)/5


