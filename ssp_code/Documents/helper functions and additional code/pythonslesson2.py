from math import*
import numpy as np
import matplotlib.pyplot as plt
##
##
###NxN matrix
##def NXN (n):
##    m1 = np.zeros((n,n))
##    for rows in range (n):
##        for cols in range (n):
##            m1[rows][cols] = (rows+1)*10 + cols+1
##    return m1
##
####print(NXN(10))
##
###det3x3
##
##def det3x3 (m):
##    v1 = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
##    v2 = m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])
##    v3 = m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
##
##    return v1 - v2 + v3
##
####M = np.array([[1,2,3],[4,5,6],[7,8,9]])
####print(det3x3(M))
##    
###make plots of sin cos sin*cos
##
##
##x1 = np.arange(-2*pi, 2*pi, 0.02)
##y1 = np.sin(x1)
##y2 = np.cos(x1)
##y3 = y1 * y2
##A = 1
##s = 4
##y4  = A*np.exp(-(x1)**2/s)
##
##plt.plot(x1, y1, 'r-', x1, y2, 'g-', x1, y3, 'b-', x1, y4, 'k-')
##plt.axis('equal')
##plt.show()


#blurry star
m1 = np.zeros((10,10))
x1 = np.arange(-5, 5, .05)
y1 = np.exp(-(x1)**2/4)
y2 = np.exp(-(x1)**2/4)
for rows in range (-5,5):
    for cols in range (-5,5):
        m1[rows][cols] = int(y1[rows] * y1[cols] *1000000)

print (m1)
        
        
