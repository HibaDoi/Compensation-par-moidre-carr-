from math import *
from statistics import mean
import numpy as np
nu=1
def delta(a,b):
    return b-a
def d(X1,Y1,X2,Y2):
    return sqrt(delta(X1,X2)**2+delta(Y1,Y2)**2)
def Gt(X1,Y1,X2,Y2):
    deltax=delta(X1,X2)
    print("deltax",deltax)
    deltay=delta(Y1,Y2)
    print("deltay",deltay)
    if deltax>=0 and deltay>=0:
        return atan(deltax/deltay)*200/pi
    elif deltax>=0 and deltay<=0:
        return atan(abs(deltay/deltax))*200/pi+100
    elif deltax<=0 and deltay<=0:
        return atan(deltax/deltay)*200/pi+200
    elif deltax<=0 and deltay>=0:
        return atan(abs(deltay/deltax))*200/pi+300

def rp(s):
    if s <0:
        s+=400
    elif s> 400:
        s-=400
    return s
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)
def dr(X1,Y1,X2,Y2):
    return delta(X2,X1)/singr(Gt(X1,Y1,X2,Y2))
XAV=365793.6900
YAV=377101.7200
XSK=364824.4300
YSK=375997.9300
XAC=364767.9600
YAC=373965.4400
XM=364413.9560
YM=376098.5763
XENTA=364370.21
YENTA=376076.10
XProjSO=362154.53
YprojSO=374493.02
XmosqM=361977.97
YmosqM=375472.19
Xtopo18=364380.68
Ytopo18=376131.72
Xmosq2=363236.12
Ymosq2=377657.88

GTMAV=Gt(XM,YM,XAV,YAV)
GTMSK=Gt(XM,YM,XSK,YSK)
GTMAC=Gt(XM,YM,XAC,YAC)
GTMENTA=Gt(XM,YM,XENTA,YENTA)
GTMProjSO=Gt(XM,YM,XProjSO,YprojSO)
GTMMosqM=Gt(XM,YM,XmosqM,YmosqM)
GTMtopo18=Gt(XM,YM,Xtopo18,Ytopo18)
GTMmosq2=Gt(XM,YM,Xmosq2,Ymosq2)

alpha=[]
alpha.append(GTMAV)
alpha.append(GTMSK)
alpha.append(GTMAC)
alpha.append(GTMENTA)
alpha.append(GTMProjSO)
alpha.append(GTMMosqM)
alpha.append(GTMtopo18)
alpha.append(GTMmosq2)

##DISTANCE
DMAV=d(XM,YM,XAV,YAV),dr(XM,YM,XAV,YAV)
DMSK=d(XM,YM,XSK,YSK),dr(XM,YM,XSK,YSK)
DMAC=d(XM,YM,XAC,YAC),dr(XM,YM,XAC,YAC)
DMENTA=d(XM,YM,XENTA,YENTA),dr(XM,YM,XENTA,YENTA)
DMProjSO=d(XM,YM,XProjSO,YprojSO),dr(XM,YM,XProjSO,YprojSO)
DMMosqM=d(XM,YM,XmosqM,YmosqM),dr(XM,YM,XmosqM,YmosqM)
DMtopo18=d(XM,YM,Xtopo18,Ytopo18),dr(XM,YM,Xtopo18,Ytopo18)
DMmosq2=d(XM,YM,Xmosq2,Ymosq2),dr(XM,YM,Xmosq2,Ymosq2)

alphaD=[]
alphaD.append(DMAV)
alphaD.append(DMSK)
alphaD.append(DMAC)
alphaD.append(DMENTA)
alphaD.append(DMProjSO)
alphaD.append(DMMosqM)
alphaD.append(DMtopo18)
alphaD.append(DMmosq2)


LMAV=0
LMSK=55.3290
LMAC=129.5518
LPS=200.6890
LMM=223.9979
LM2=298.8371
DENTA=49.196
Dtopo18=46.635
Lang=[]
Lang.append(LMAV)
Lang.append(LMSK)
Lang.append(LMAC)
Lang.append(LPS)
Lang.append(LMM)
Lang.append(LM2)


VOAV=GTMAV-0
VOSK=GTMSK-LMSK
VOAC=GTMAC-LMAC
VOPS=GTMProjSO-LPS
VOMM=GTMMosqM-LMM
VOM2=GTMmosq2-LM2
VO=[]
VO.append(VOAV)
VO.append(VOSK)
VO.append(VOAC)
VO.append(VOPS)
VO.append(VOMM)
VO.append(VOM2)

VOm=mean(VO)
DG=VOAC-VOm
