from math import cos , sin , tan, atan , pi , sqrt


def delta(a,b):
    return b-a

def cotangr(x):
    return 1/tan(x*pi/200)



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

def d(X1,Y1,X2,Y2):
    return sqrt(delta(X1,X2)**2+delta(Y1,Y2)**2)
def cosgr(x):
    return cos(x*pi/200)
def singr(x):
    return sin(x*pi/200)
def rp(s):
    if s <0:
        s+=400
    elif s> 400:
        s-=400
    return s

X=[363236.1200,364951.7600,365793.0900]
Y=[377657.8800,377249.9400,377101.7200]

alpha=68.30680
beta= 100.47560-68.30680
GtMB=atan(((X[0]-X[1])*cotangr(alpha)-(X[2]-X[1])*cotangr(beta)+(Y[2]-Y[0]))/((Y[0]-Y[1])*cotangr(alpha)-(Y[2]-Y[1])*cotangr(beta)+(X[2]-X[0])))*200/pi
GTBM=rp(GtMB+200)
GtBA=Gt(X[1],Y[1],X[0],Y[0])
aph=GtBA-GTBM
bet=200-alpha-aph
BA=d(X[1],Y[1],X[0],Y[0])
BM=BA*singr(bet)/sin(alpha)
xm=X[1]+BM*singr(GTBM)
ym=Y[1]+BM*cosgr(GTBM)
print(round(xm,2),round(ym,2))




print(364420.5108,376084.4988)