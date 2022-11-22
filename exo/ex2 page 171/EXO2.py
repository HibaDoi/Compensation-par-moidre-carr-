

import numpy as np
A=np.matrix([[0.1,-0.0165],[0.1,0.0038],[0.1,0.0100]])

B=np.matrix([[-49.2611,0,0,0,0],[0,49.2611,0,-0.1,0],[0,0,49.2611,-0.1,-0.1]])

W=np.matrix([[0],[0],[-0.4944]])
i=10**7
P=np.matrix([[2.5*i,0,0,0,0],
              [0,2.5*i,0,0,0],
              [0,0,2.5*i,0,0],
              [0,0,0,1,0],
              [0,0,0,0,1]])
X0=np.matrix([[8.1208],[49.2611]])
L=[[0.0165],
   [0.0038],
   [0.01],
   [10],
   [8]]
I3=np.identity(3)
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
Qk=M_1*(I3-A*(N_1)*A_T*M_1)
Ck=sigma0_2*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0_2*Qv
Ql=P_1-Qv
Cl=sigma0_2*Ql



