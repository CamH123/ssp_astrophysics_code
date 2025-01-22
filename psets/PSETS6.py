from math import*
import numpy as np
import matplotlib.pyplot as plt


#PSET 6
# PS6-2
def mag(x, y):
    return((x**2 + y**2)**.5)
#62A
##def randomWalk(N,r):
##    xpos = 0
##    ypos = 0
##    distSqSum = 0
##    for i in range(N):
##        direction = np.random.rand()
##        plt.grid(True)
##        if direction <= .25:
##            xpos -= r
##        elif direction <= .5:
##            xpos += r
##        elif direction <= .75:
##            ypos+= r
##        else:
##            ypos -= r
##        distSqSum += mag(xpos, ypos)**2
##        plt.plot(xpos, ypos, 'o', color = 'green')
##        plt.axis('equal')
##        plt.pause(.01)
##
##        
##    plt.show()
##    print((distSqSum/N)**.5)
##    print((N**.5)*r)
##
##
##    return ((distSqSum / N)**.5)
##
##def randomWalk(N,r):
##    xpos = 0
##    ypos = 0
##    distSqSum = 0
##    for i in range(N):
##        direction = np.random.rand() * 2 * pi
##        xpos += np.cos(direction) * r
##        ypos += np.sin(direction) * r
##        plt.grid(True)
##        plt.plot(xpos, ypos, 'o', color = 'green')
##        plt.axis('equal')
##        plt.pause(.01)
##    print((distSqSum/N)**.5)
##    print((N**.5)*r)
##
##    return (mag(xpos, ypos))
##print(randomWalk(100, 1))
##
##def rms (t, N ,r):
##    sumSq = 0
##    dists = np.array([])
##    for i in range(t):
##        walk = randomWalk(N,r)
##        sumSq += walk**2
##        dists = np.append(dists, walk)
##        
##    sumSq = (sumSq/t)**.5
##    plt.hist(dists)
##    plt.show()
##    return(sumSq)
##print('exp value: ', rms(500,500,1))
##print('rootnr value: ', 500**.5)


#PS6-8
def centroid(data):
    M = data
    Xcm = 0
    sumnx = 0
    sumn = 0
    sumny = 0
    N = np.sum(M)
    for y in range(len(data)):
        for i in range(len(data)):
            sumn += M[y][i]
            sumny += M[y][i] * y
            #N += M[y][i]
    Ycm = sumny / sumn

    for x in range(len(data)):
        for j in range(len(data)):
            sumnx += M[j][x] * x
            
    Xcm = sumnx / sumn

    xicm = 0
    yicm = 0

    for row in range(len(M)):
        for col in range(len(M)):
            xicm += ((row - Xcm)**2)*M[row][col]
            yicm += ((col - Ycm)**2)*M[row][col]
    delX = (xicm**.5)/N
    delY = (yicm**.5)/N
    

    
    map = plt.imshow(M) #M is your np.array of the photon counts
    plt.colorbar(map)
    plt.plot(Xcm, Ycm,'+') #Xcm, Ycm are centroid coordinates
    plt.show()

    print(delX)
    print(delY)
    return Xcm, Ycm, delX, delY


data = np.loadtxt('/home/chuang/Downloads/centroidData.csv', dtype=float,delimiter=',')
Xcm, Ycm, xicm, yicm = centroid(data)
print('Xcm: ', round(Xcm, 2), ' delX: ', round(xicm, 2))
print('Ycm: ', round(Ycm, 2), ' delY: ', round(yicm, 2))




