from math import*
import numpy as np
import matplotlib.pyplot as plt

def RAdecToHMS(RA):
    hours = int(RA/15)
    minutes = int((RA-hours*15)/.25)
    seconds = (RA-hours*15-minutes*.25)*240
    return(hours, minutes, seconds)

def HMStoDeg(hours, minutes, seconds, dOr):

    deg = (hours/24)*360 + (minutes/(24*60))*360 + (seconds/(24*3600))*360
    deg %= 360
    if dOr == False:
        return (deg)
    else:
        return (deg * pi /180)

def DMStoDeg(degrees, arcmin, arcsec):
    pos = copysign(1,degrees)
    bos = copysign(1,arcmin)
    if pos >= 1 and bos >= 0:
        deg = degrees + arcmin/60 + arcsec/3600
        #deg %= 360
        return (deg)
        
    elif(pos <= 1 and bos >= 1):
        deg = degrees - arcmin/60 - arcsec/3600
        #deg %= 360
        return (deg)
    elif (pos <=1 and bos <=1):
        deg = degrees + arcmin/60 + arcsec/3600
        #deg %= 360
        return (deg)
        
    else:
        deg = degrees - arcmin/60 - arcsec/3600
        #deg %= 360
        return (deg)
        

def DECdecToDMS(dec):
    degSign = copysign(1, dec)
    if degSign < 0:
        deg = float(ceil(dec))
        minutes = float(ceil((dec-deg)*60))
    else:
        deg = floor(dec)
        minutes = floor(((dec-deg)*60))
    seconds = float(((dec-deg-(minutes/60))*3600))
    print('sec is ' , seconds)
    if deg == 0 and (minutes <0 or seconds < 0):
        deg = -0.0
    minutes = abs(minutes)
    seconds = abs(seconds)
    return(deg, int(minutes), seconds)

def dot (v1, v2):
    sum  = 0
    for i in range(3):
       sum = sum + v1[i] * v2[i]
    return sum

def mag(v1):
    return((v1[0]**2 + v1[1]**2 + v1[2]**2)**.5)

def quadcheck(so, co):
    if (so >= 0):
        return np.arccos(co)
    else:
        return 2*pi - np.arccos(co)

def cross(v1, v2):
    vect = np.array([])
    vect = np.append(vect,v1[1]*v2[2]-v1[2]*v2[1])
    vect = np.append(vect, (-1)*(v1[0]*v2[2]-v1[2]*v2[0]))
    vect = np.append(vect, v1[0]*v2[1]-v1[1]*v2[0])
    return vect

def NewtonRaphson(f, deri, intGuess, error ):
    xi = intGuess
    i = 0
    xi2 = xi - (f(xi)/deri(xi))
    while (abs(xi - xi2) >error and i < 10000):
        xi = xi2
        xi2 = xi - (f(xi)/deri(xi))
        
        i+= 1
    return(xi)

def rotMatrix(vect1, a, b, c):
    rot1 = np.array([[cos(a), -sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1]])
    rot2 = np.array([[1, 0, 0], [0, cos(b), -sin(b)], [0, sin(b), cos(b)]])
    rot3 = np.array([[cos(c), -sin(c), 0], [sin(c), cos(c), 0], [0, 0, 1]])
    
    return rot1 @ rot2 @ rot3 @ vect1


#ODcode1
def angMomentum(x1, v1):
    return cross(x1, v1)


#ODcode2: a, e, i ,Omega, w
def od1(x1, v1):
    a = 1 / (2/mag(x1) - mag(v1)**2)
    h = angMomentum(x1, v1)
    e = (1-(mag(h)**2)/a)**.5
    i = np.arctan(((h[0]**2 + h[1]**2)**.5)/h[2])
    #i = h[2]/mag(h)
    
    cosLong = (-h[1]/(mag(h)*np.sin(i)))
    sinLong = h[0] / (mag(h) * np.sin(i))
    longAscen = quadcheck(sinLong, cosLong)
    
    cosU = (x1[0]*cosLong + x1[1]*sinLong)/mag(x1)
    sinU = x1[2]/(mag(x1)*sin(i))
    U = quadcheck(sinU, cosU)# * 180 / pi
    cosV = (1/e)*((a*(1-e**2))/mag(x1) - 1)
    sinV = ((a*(1-e**2))/(mag(h)*e)) * (dot(x1, v1))/mag(x1)
    v = quadcheck(sinV, cosV) #* 180 / pi 
    w = U - v
    w %= 2 * pi
    
    cosE = (e + cosV)/(1+e*cosV)
    sinE = (mag(x1)*sinV)/(a*(1-e**2)**.5)
    E = quadcheck(sinE, cosE)
    M = E - e*sinE 
    #t = 2458313.500000000  *2 * pi / 365.25689832
    t = 2458313.5
    k = 0.01720209894
    n = k / (a**3/2)

    T = t - M/n
        
    return(a, e, i, longAscen, w, M, T, E, v)

def error(act, expect):
    return(abs(((act - expect)/expect) * 100))
    
    
data = np.loadtxt('/home/chuang/Downloads/huangInput.csv', dtype=float,delimiter=',')

x1 = np.array([data[0], data[1], data[2]])
v1 = np.array([data[3], data[4], data[5]])
v1 *= 365.257/(2*pi) 

a, e, i, lA, w, M, T, E, v = od1(x1, v1)

sunVect = np.array([-.6574011189521245, .7730192934005375, -3.334040102015075*10**(-5)])

print('A: ', a, '%error ', error(a, 1.056800055731616))
print('e: ', e, '%error ', error(e, .3442331093555991))
print('i: ', i * 180 / pi, '%error ', error(i * 180 / pi, 25.15525166261175))
print('lA: ', lA * 180 / pi, '%error ', error(lA * 180 / pi, 236.237980644942))
print('w: ', w * 180 / pi, '%error ', error(w * 180 / pi, 255.5046142848255))
print('M: ', M * 180 / pi, '%error ', error(M * 180 / pi, 140.4194576391787))
print('T: ', T, '%error ', error(T , 2458158.720849529840))


def ephm(a, e, i, lA, w, M, T, date, sunVect):
    k = 0.01720209894
    n = k / (a**1.5)
    #T = 2458158.720849529840
    m1 = n * (date - T)
    print(m1, n, a)

    E = NewtonRaphson(lambda x:m1 - (x - e*np.sin(x)), lambda x: e*np.cos(x) - 1, m1, 10**(-9))

    pos = np.array([a*np.cos(E) - a*e, a*((1-e**2)**.5)*np.sin(E), 0])
    rotR = rotMatrix(pos, lA, i, w)


    eqMat = np.array([[1, 0, 0], [0, cos(23.44*pi/180), -sin(23.44*pi/180)], [0, sin(23.44*pi/180), cos(23.44*pi/180)]])
    p = rotR + sunVect
    p = eqMat @ p

    pmag = (p[0]**2 + p[1]**2 + p[2]**2)**.5
    dec = np.arcsin(p[2] / pmag)
    cosa = (p[0] / pmag)/cos(dec)
    sina = (p[1] / pmag)/cos(dec)
    ra = quadcheck(sina, cosa)
    print(degrees(ra))
    print(degrees(dec))
    return(ra, dec)

ra, dec = ephm(a, e, i , lA, w, M, T, 2458333.500000000, sunVect)
print('ra: ', RAdecToHMS(ra* 180/pi), ' dec: ', DECdecToDMS(dec * 180 / pi))
print('r error ', error(ra, HMStoDeg(17, 42, 21.12, True)), ' dec error ', error(dec, DMStoDeg(31, 52, 26.8) * pi / 180))
    
    
    










