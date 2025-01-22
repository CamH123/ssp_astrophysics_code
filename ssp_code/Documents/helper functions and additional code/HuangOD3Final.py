from math import*
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

#converts RA from decimal to hours/minutes/seconds
def RAdecToHMS(RA):
    hours = int(RA/15)
    minutes = int((RA-hours*15)/.25)
    seconds = (RA-hours*15-minutes*.25)*240
    return(hours, minutes, seconds)

#converts RA from hours/minutes/seconds to decimal
def HMStoDeg(hours, minutes, seconds, dOr):
    deg = (hours/24)*360 + (minutes/(24*60))*360 + (seconds/(24*3600))*360
    deg %= 360
    if dOr == False:
        return (deg)
    else:
        return (deg * pi /180)

#converts angles from degrees to decimals
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
        
#Converts declination from decimal to deg, min, sec
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

#Dot product
def dot (v1, v2):
    sum  = 0
    for i in range(3):
       sum = sum + v1[i] * v2[i]
    return sum

#magnitutde of 3 terms
def mag(v1):
    return((v1[0]**2 + v1[1]**2 + v1[2]**2)**.5)

#Determines quadrant of angle
def quadcheck(so, co):
    if (so >= 0):
        return np.arccos(co)
    else:
        return 2*pi - np.arccos(co)

#Cross Product
def cross(v1, v2):
    vect = np.array([])
    vect = np.append(vect,v1[1]*v2[2]-v1[2]*v2[1])
    vect = np.append(vect, (-1)*(v1[0]*v2[2]-v1[2]*v2[0]))
    vect = np.append(vect, v1[0]*v2[1]-v1[1]*v2[0])
    return vect

#NewtonRaphson Method
def NewtonRaphson(f, deri, intGuess, error ):
    xi = intGuess
    i = 0
    xi2 = xi - (f(xi)/deri(xi))
    while (abs(xi - xi2) >error and i < 10000):
        xi = xi2
        xi2 = xi - (f(xi)/deri(xi))
        
        i+= 1
    return(xi)

#Rotates vectors for ephm
def rotMatrix(vect1, a, b, c):
    rot1 = np.array([[cos(a), -sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1]])
    rot2 = np.array([[1, 0, 0], [0, cos(b), -sin(b)], [0, sin(b), cos(b)]])
    rot3 = np.array([[cos(c), -sin(c), 0], [sin(c), cos(c), 0], [0, 0, 1]])
    return rot1 @ rot2 @ rot3 @ vect1

#Calculates vector for angular Momentum
def angMomentum(x1, v1):
    return cross(x1, v1)

#Takes pos and vel vector, and returns 6 orbital elements
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

#Converts caldendar day to julian day
def cdToJd(y, m, d):
    a = 367 * y
    b = int(((int((m+9)/12) + y) * 7)/4)
    return a - b + int((275*m)/9) + d + 1721013.5

def timeDMS (h, m, s):
    return ((h/24) + m/(24*60) + s/(24*60*60))

def montCarlo (fieldRA, indexRA, fieldDec, indexDec, objNum):
    sumRA = 0
    sumDec = 0
    for i in range(objNum):
        sumRA += (fieldRA[i] - indexRA[i])**2
        sumDec+= (fieldDec[i] - indexDec[i])**2
    sdRA = (sumRA/objNum)**.5
    sdDec = (sumDec/objNum)**.5
    
    return sdRA, sdDec


def ephm(a, e, i, lA, w, M, T, date, sunVect):
    k = 0.01720209894
    n = k / (a**1.5)
    #T = 2458158.720849529840
    m1 = n * (date - T)
    print(m1, n, a)

    E = NewtonRaphson(lambda x:m1 - (x - e*np.sin(x)), lambda x: e*np.cos(x) - 1, m1, 10**(-9))

    pos = np.array([a*np.cos(E) - a*e, a*((1-e**2)**.5)*np.sin(E), 0])
    rotR = rotMatrix(pos, lA, i, w)

    eqMat = np.array([[1, 0, 0], [0, cos(23.4374*pi/180), -sin(23.4374*pi/180)], [0, sin(23.4374*pi/180), cos(23.4374*pi/180)]])
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

def orgData(data, obs):
    date = np.array([])
    ra = np.array([])
    dec = np.array([])
    sunVect = np.array([])
    
    for i in obs:
        date = np.append(date, cdToJd(data[i][0], data[i][1], data[i][2]) + timeDMS(data[i][3], data[i][4], data[i][5]))
        ra = np.append(ra, [data[i][6], data[i][7], data[i][8]])
        dec = np.append(dec, [data[i][9], data[i][10], data[i][11]])
        sunVect = np.append(sunVect, np.array([data[i][12], data[i][13], data[i][14]]))
       
    return(date, ra, dec, sunVect)

def FandG(r, rdot, tau):
    f1 = 1-((tau**2)/(2*mag(r)**3))
    f2 = ((dot(r, rdot)*tau**3)/(2*mag(r)**5))
    f3 = ((tau**4)/(24*mag(r)**3))
    
   

    f4 = 3*((dot(rdot, rdot)/(mag(r)**2))-(1/(mag(r)**3)))
    f5 = 15*(((dot(r, rdot))/(mag(r)**2))**2)
    f6 = 1/(mag(r)**3)

    fb = f4 - f5 + f6
    ft = f1 + f2 + f3 * fb

    g1 = tau - ((tau**3)/(6*(mag(r)**3))) + ((dot(r, rdot) * (tau**4))/(4*(mag(r)**5)))

    return ft, g1


def mog (ras, decs, t1, t2, t3, sunVects):
    #testing(hardcode time)
    # t1 = 2460118.708333333
    # t2 = 2460120.772916667
    # t3 = 2460122.768055555
    
    
    #constant
    cAU = 173.144643267 * 365.25 / (2*pi)
    
    ra1 = HMStoDeg(ras[0], ras[1],ras[2],True)
    ra2 = HMStoDeg(ras[3], ras[4],ras[5], True)
    ra3 = HMStoDeg(ras[6], ras[7],ras[8], True)
    #print(ra1, ra2, ra3)
    
    dec1 = DMStoDeg(decs[0], decs[1], decs[2]) * pi / 180
    dec2 = DMStoDeg(decs[3], decs[4], decs[5])* pi / 180
    dec3 = DMStoDeg(decs[6], decs[7], decs[8])* pi / 180
    
    ph1 = np.array([cos(ra1) * cos(dec1), sin(ra1)*cos(dec1), sin(dec1)])
    ph2 = np.array([cos(ra2) * cos(dec2), sin(ra2)*cos(dec2), sin(dec2)])
    ph3 = np.array([cos(ra3) * cos(dec3), sin(ra3)*cos(dec3), sin(dec3)])
    #print('ph', ph1, ph2, ph3)
    k = 0.0172020989484 #Gaussin
    
    t1=t1*k
    t2=t2*k
    t3=t3*k
    t1a = t1
    t2a = t2
    t3a = t3
    
    
    tau1 =  (t1 - t2)
    tau0 =  (t3 -t1)
    tau3 =  (t3 - t2)
    
    a1 = tau3 / tau0
    a3 = -tau1 / tau0
    
    sunR1 = np.array([sunVects[0], sunVects[1], sunVects[2]])
    sunR2 = np.array([sunVects[3], sunVects[4], sunVects[5]])
    sunR3 = np.array([sunVects[6], sunVects[7], sunVects[8]])
    
    p1 = (a1 * dot((cross(sunR1, ph2)), ph3) - dot(cross(sunR2, ph2), ph3) + a3*(dot(cross(sunR3, ph2), ph3))) / (a1 * (dot(cross(ph1, ph2), ph3)))
    p2 = (a1 * dot((cross(ph1, sunR1)), ph3) - dot(cross(ph1, sunR2), ph3) + a3*(dot(cross(ph1, sunR3), ph3))) / (-1*(dot(cross(ph1, ph2), ph3)))
    p3 = (a1 * dot((cross(ph2, sunR1)), ph1) - dot(cross(ph2, sunR2), ph1) + a3*(dot(cross(ph2, sunR3), ph1))) / (a3 * (dot(cross(ph2, ph3), ph1)))
    
    r1 = p1 * ph1 - sunR1
    r2 = p2 * ph2 - sunR2
    r3 = p3 * ph3 - sunR3
    #print(r1, r2, r3)
    v12 = (r2 - r1)/(t2- t1)
    v23 = (r3 - r2)/(t3-t2)
    
    rd2 = ((t3-t2)*v12 + (t2-t1)*v23)/(t3 - t1)
    f1, g1 = FandG(r2, rd2, tau1)
    f3, g3 = FandG(r2, rd2, tau3)
    
    a1 = g3/(f1*g3 - f3 * g1)
    a3 = -g1/(f1*g3 - f3*g1)
    #print('a1: ', a1, 'a3', a3)
    count = 0
    r20 = r2*1000
    
    while count < 10000 and abs((mag(r2)-mag(r20))/mag(r2)) > 10**(-10):
        r20 = r2
        p1 = (a1 * dot((cross(sunR1, ph2)), ph3) - dot(cross(sunR2, ph2), ph3) + a3*(dot(cross(sunR3, ph2), ph3))) / (a1 * (dot(cross(ph1, ph2), ph3)))
        p2 = (a1 * dot((cross(ph1, sunR1)), ph3) - dot(cross(ph1, sunR2), ph3) + a3*(dot(cross(ph1, sunR3), ph3))) / (-1*(dot(cross(ph1, ph2), ph3)))
        p3 = (a1 * dot((cross(ph2, sunR1)), ph1) - dot(cross(ph2, sunR2), ph1) + a3*(dot(cross(ph2, sunR3), ph1))) / (a3 * (dot(cross(ph2, ph3), ph1)))
        
        r1 = p1 * ph1 - sunR1
        r2 = p2 * ph2 - sunR2
        r3 = p3 * ph3 - sunR3
        
        r2 = (g3*r1 - g1*r3)/(f1*g3 - f3*g1)
        rd2 = (f3*r1 - f1*r3)/(f3*g1 - f1*g3)
        
        f1, g1 = FandG(r2, rd2, tau1)
        f3, g3 = FandG(r2, rd2, tau3)
        
        a1 = g3/(f1*g3 - f3 * g1)
        a3 = -g1/(f1*g3 - f3*g1)
        
        #light travel correction
        t1 = t1a - p1/cAU
        t2 = t2a - p2/cAU
        t3 = t3a - p3/cAU
        
        tau1 =  (t1 - t2)
        tau0 =  (t3 -t1)
        tau3 =  (t3 - t2)
        
        
        count += 1
    eqMat = np.array([[1, 0, 0], [0, cos(-23.4374*pi/180), -sin(-23.4374*pi/180)], [0, sin(-23.4374*pi/180), cos(-23.4374*pi/180)]])
    r2 = eqMat@r2
    rd2 = eqMat@rd2
    
    
    return r2, rd2, p2


        
        

data = np.loadtxt('/home/chuang/Downloads/huangInput.csv', dtype=float,delimiter=',')
dates, ras, decs, sunVects = orgData(data, [7,8,9])
print(dates)
r2, rd2, p = mog(ras, decs, dates[0], dates[1], dates[2], sunVects)
print(r2, rd2)
a, e, i, longAscen, w, M, T, E, v = od1(r2, rd2)
ra, dec = ephm(a, e, i, longAscen, w, M, 2460147.666680342518, 2460135.764583333, [-3.049251837806797E-01, 9.698714474392726E-01, -8.769385382108086E-05])
print('ra: ', ra * 180 / pi, 'dec: ', dec * 180/pi)
print('position ', r2)
print('velocity ', rd2)
print('range: ', p)
print('a ', a)
print('e ', e)
print('i: ', i * 180 / pi)
print('longAscen: ', longAscen * 180 / pi)
print('w: ', w * 180 / pi)
print('M: ', M * 180 / pi)

table = fits.open('/home/chuang/Downloads/corr.fits')[1].data

fieldRA = table.field_ra
indexRA = table.index_ra
fieldDec = table.field_dec
indexDec = table.index_dec


numObj = int(table.shape[0])
sdRA, sdDec = montCarlo(fieldRA, indexRA, fieldDec, indexDec, numObj)
print(sdRA, sdDec)


    
    
    
    
    
    










