# PS1 - 13
from math import *

def HMStoDeg(hours, minutes, seconds, dOr):

    deg = (hours/24)*360 + (minutes/(24*60))*360 + (seconds/(24*3600))*360
    deg %= 360
    if dOr == False:
        return (deg)
    else:
        return (deg * pi /180)
        

# PS1-14 A
def dot (v1, v2):
    sum  = 0
    for i in range(3):
       sum = sum + v1[i] * v2[i]
    return sum

# PS1-14 B
def cross(v1, v2):
    vect = []
    vect.append(v1[1]*v2[2]-v1[2]*v2[1])
    vect.append((-1)*(v1[0]*v2[2]-v1[2]*v2[0]))
    vect.append(v1[0]*v2[1]-v1[1]*v2[0])
    return vect

# PS1-14 C
def triProd(v1, v2, v3):
    return dot(v1, cross(v2, v3))
    

#Test HMS
HMStoDeg(10, 10, 10, False)

#Test dot
print (dot([1,2,3], [3,4,5]))

#Test Cross
print(cross([1,2,3], [3,4,5]))

#Test triProd
print(triProd([1,2,3], [3,4,5], [5,-6,7]))
