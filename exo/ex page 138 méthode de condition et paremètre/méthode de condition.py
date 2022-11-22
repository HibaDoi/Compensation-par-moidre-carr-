
import numpy as np
B=np.matrix([[-1,0,-1,1],[-1,-1,0,1]])

W=np.matrix([[0.03],[0.01]])
P=np.identity(4)
L=np.matrix([[100.010],   
   [200.050] ,
   [300.090],
   [100.020]])

P_1=np.linalg.inv(P)
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)
I4=np.identity(4)





K=-M_1*(W)
V=P_1*B_T*K
Les=L+V
sigma0_2=(0.05)**2
V_T=V.transpose()

I4=np.identity(4)
Qk=M_1
Qv=P_1*B_T*Qk*B*P_1

Ql=P_1-Qv
Cl=sigma0_2*Ql
sigma0es=(V_T*P*V)/4



