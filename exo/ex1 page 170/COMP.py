# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:52:12 2022

@author: hp
"""

import numpy as np
A=np.matrix([[1],[1]])
B=np.matrix([[3.335,0,2.669],[0,-3.335,2.668]])
W=np.matrix([[0],[-0.033]])
P=np.matrix([[2.78,0,0],
              [0,1.78,0],
              [0,0,1]])

P_1=np.linalg.inv(P)
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)
A_T=A.transpose()
N=A_T*M_1*A
N_1=np.linalg.inv(N)
N_W=A_T*M_1*W
X=-1*N_1*N_W
