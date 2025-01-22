from math import*
import numpy as np
import matplotlib.pyplot as plt



def cross(v1, v2):
    vect = np.array([])
    vect = np.append(vect,v1[1]*v2[2]-v1[2]*v2[1])
    vect = np.append(vect, (-1)*(v1[0]*v2[2]-v1[2]*v2[0]))
    vect = np.append(vect, v1[0]*v2[1]-v1[1]*v2[0])
    return vect


#ODcode1
def angMomentum(x1, v1):
    return cross(x1, v1 *365.257/(2*pi))
    
data = np.loadtxt('/home/chuang/Downloads/huangInput.csv', dtype=float,delimiter=',')

x1 = np.array([data[0], data[1], data[2]])
v1 = np.array([data[3], data[4], data[5]])

print(np.round(angMomentum(x1, v1), 6))


