from math import*
import numpy as np
import matplotlib.pyplot as plt

def dot (v1, v2):
##    sum  = 0.0
##    for i in range(3):
##       sum = sum + v1[i] * v2[i]
##    return sum
    x = v1[0] * v2[0]
    y = v1[1] * v2[1]
    z = v1[2] * v2[2]
    return(x+y+z)

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


print(FandG([0.26662393644794813, -1.381475976476564, -0.5048589337503169], [0.8442117090940343, -0.39728396707075087, 0.14202728258915864],-0.3261857571141891))
print(FandG([0.26662393644794813, -1.381475976476564, -0.5048589337503169], [0.8442117090940343, -0.39728396707075087, 0.14202728258915864],0.05084081855693949)) 



