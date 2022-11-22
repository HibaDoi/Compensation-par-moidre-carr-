from math import *
import numpy as np
nu=2
#Matrice A
A=np.matrix([[0.0159],[0.0159],[0.0159]])
#Matrice B est égale a la négation
B=-np.identity(3)
W=np.matrix([[0],[-0.09],[-0.21]])
CL=np.matrix([[(0.02)**2,0,0,],
              [0,(0.04)**2,0],
              [0,0,(0.08)**2]])
sigma0=(0.08)**2
P=sigma0*np.linalg.inv(CL)

S0=np.matrix([[314.788]])
L=[[10.01],
   [10.10],
   [10.22]]
I3=np.identity(3)
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
sigma0_2=(0.08)**2
V_T=V.transpose()
sigma0es=(V_T*P*V)/nu
Cx=sigma0_2*N_1
Qk=M_1*(I3-A*(N_1)*A_T*M_1)
Ck=sigma0_2*Qk
Qv=P_1*B_T*Qk*B*P_1
Cv=sigma0_2*Qv
Ql=P_1-Qv
Cl=sigma0_2*Ql



