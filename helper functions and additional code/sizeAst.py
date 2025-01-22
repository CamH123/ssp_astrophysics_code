from math import*
import numpy as np
import matplotlib.pyplot as plt

def dot (v1, v2):
    sum  = 0
    for i in range(3):
       sum = sum + v1[i] * v2[i]
    return sum

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

def mag(v1):
    return((v1[0]**2 + v1[1]**2 + v1[2]**2)**.5)

def phi(a, b, alpha):
    return(e**(-a*(tan(0.5*alpha)*b)))

rVect = np.array([5.363157809222286E-01, -1.105820062566023, 1.117812351469707E-01])
print(mag(rVect))
deltaVect = np.array([1.876027055165577E-01, -1.509014996479809E-01, 1.117341500917547E-01])
print(mag(deltaVect))
sina = mag(cross(deltaVect, rVect))/(mag(rVect) * mag(deltaVect))
cosa = dot(rVect, deltaVect) / (mag(rVect) * mag(deltaVect))

a = quadcheck(sina, cosa)
print('a', a)

A1 = 3.33
A2 = 1.87
B1 = 0.63
B2 = 1.22
G = 0.15

HA = 16.883 - 5 * log(mag(rVect) * mag(deltaVect), 10)

print('ha', HA)

#a = a * 180 / pi

phil1 = phi(A1, B1, a)
phil2 = phi(A2, B2, a)



H = HA + 2.5*log((1-G)*phil1+ G*phil2, 10)
#H = 22.1
print('h', H)

D = 1329 * (10**(-0.2*H)) *( .15**(-.5))
print('d', D)

