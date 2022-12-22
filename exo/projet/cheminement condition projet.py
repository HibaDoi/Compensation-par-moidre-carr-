
from math import *
from statistics import mean
import numpy as np
np.set_printoptions(precision=4,suppress=True)
#fonction de différence
def delta(a,b):
    return b-a
#fonction de la distance
def d(X1,Y1,X2,Y2):
    return sqrt(delta(X1,X2)**2+delta(Y1,Y2)**2)
#fonction de gisement 
def Gt(X1,Y1,X2,Y2):
    deltax=delta(X1,X2)
    #print("deltax",deltax)
    deltay=delta(Y1,Y2 )
    #print("deltay",deltay)
    if deltax>=0 and deltay>=0:
        return atan(deltax/deltay)*200/pi
    elif deltax>=0 and deltay<=0:
        return atan(abs(deltay/deltax))*200/pi+100
    elif deltax<=0 and deltay<=0:
        return atan(deltax/deltay)*200/pi+200
    elif deltax<=0 and deltay>=0:
        return atan(abs(deltay/deltax))*200/pi+300
#fonction de parametrage des angle
def rp(s):
    if s <0:
        s+=400
    elif s> 400:
        s-=400
    return s

R0cc=(200/pi)*10000
#sin et cos en grade
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)
'''XD=[364227.83 ,376274.66]
XA=[364320.026 , 376378.770]
XRD=[364182.270 , 376218.180]
XRA=[364284.13 , 376312.34]
angle=[240.5711,123.5289,258.2405,365.9734]
distance=[45.56,68.92,46.91]'''
XD=[364227.83 ,376274.66]
XA=[364320.026 , 376378.770]
XRD=[364182.270 , 376218.180]
XRA=[364284.13 , 376312.34]
angle=[240.5721,123.5289,258.2445,365.9745]
#distance=[45.56,68.92,46.95]
distance=[45.55,68.91,46.93]
Gd=Gt(XRD[0],XRD[1],XD[0],XD[1])
Ga=Gt(XA[0],XA[1],XRA[0],XRA[1])
tetai=[]
for i in range(len(angle)):
    tetai.append((angle[i]-200))
SommeTeta=sum(tetai)
#gisement en grades
gisement=[Gd]
for i in range(len(angle)):
    gisement.append(gisement[i]+tetai[i])
XL=[XD]
for i in range(len(angle)-1):
    XL.append([XL[i][0]+distance[i]*singr(gisement[i+1]),
                XL[i][1]+distance[i]*cosgr(gisement[i+1])])
B=[[1,1,1,1,0,0,0]]

B.append([
          XL[-1][1]-XD[1],
          XL[-1][1]-XL[1][1],
          XL[-1][1]-XL[2][1],
          0,
          XL[1][0]-XD[0],
          XL[2][0]-XL[1][0],
          XL[-1][0]-XL[2][0]])
B.append([
          XL[-1][0]-XD[0],
          XL[-1][0]-XL[1][0],
          XL[-1][0]-XL[2][0],
          0,
          XL[1][1]-XD[1],
          XL[2][1]-XL[1][1],
          XL[-1][1]-XL[2][1]])
W=[(400-(Ga-Gd-SommeTeta)-400)*10**4,-R0cc*(XA[0]-XL[-1][0]),-R0cc*(XA[1]-XL[-1][1])]
    
x=1/4
y=1/900
sigmaL=np.matrix([
    [y,0,0,0,0,0,0],
    [0,y,0,0,0,0,0],
    [0,0,y,0,0,0,0],
    [0,0,0,y,0,0,0],
    [0,0,0,0,x,0,0],
    [0,0,0,0,0,x,0],
    [0,0,0,0,0,0,x]])
P=900*sigmaL
B=np.matrix(B)  
W=np.matrix(W)
W=W.transpose()  
L=angle+distance
L=np.matrix(L)
L=L.transpose()

P_1=P
B_T=B.transpose()
M=B*P_1*B_T
M_1=np.linalg.inv(M)
I4=np.identity(4)
K=-M_1*(W)
V=P_1*B_T*K
Les=L+V
sigma0_2=196
V_T=V.transpose()

I4=np.identity(7)
Qk=M_1
Qv=P_1*B_T*Qk*B*P_1

Ql=P_1-Qv
Cl=sigma0_2*Ql
sigma0es=(V_T*P*V)/4

VDc=np.matrix([V[0,0],
              V[1,0],
              V[2,0],
              V[3,0]])

VDbeta=np.matrix([V[4,0],
              V[5,0],
              V[6,0]
              ])
VDbetaa=[]
for i in range(3):
    VDbetaa.append(VDbeta[0,i]*distance[i]/R0cc)
hatL=np.matrix(angle)+VDc*10**-4
Dc=[]
hatLd=np.matrix(distance)+VDbetaa
    
tetaic=[]
for i in range(len(angle)):
    tetaic.append((hatL[0,i]-200))
SommeTetac=sum(tetaic)
#gisement en grades
gisementc=[Gd]
for i in range(len(angle)):
    gisementc.append(gisementc[i]+tetaic[i])
gisementc=np.matrix(gisementc)
XLc=[XD]
for i in range(len(angle)-1):
    XLc.append([XLc[i][0]+hatLd[0,i]*singr(gisementc[0,i+1]),
                XLc[i][1]+hatLd[0,i]*cosgr(gisementc[0,i+1])])
    '''XL=[XD]
    for i in range(len(angle)-1):
        XL.append([XL[i][0]+distance[i]*singr(gisement[i+1]),
                    XL[i][1]+distance[i]*cosgr(gisement[i+1]")])'"''
"Qv=P_1*B_T*Qk*B*P_1

Ql=P_1-Qv
Cl=sigma0_2*Ql
sigma0es=(V_T*P*V)/4"""