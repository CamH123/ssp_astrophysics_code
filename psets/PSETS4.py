from math import*
import numpy as np
import matplotlib.pyplot as plt

#pset4

###4-7
##def leastSquaresFitting(x, y):
##    tot = np.size(x)
##    xiyisum = 0
##    xisum = 0
##    yisum = 0
##    xi2sum = 0
##    
##    for i in range(tot):
##        xiyisum += x[i]*y[i]
##        xisum += x[i]
##        yisum += y[i]
##        xi2sum += x[i]**2
##
##    m = (tot*xiyisum - xisum*yisum)/(tot*xi2sum - xisum**2)
##    b = (xi2sum*yisum - xiyisum*xisum)/(tot*xi2sum - xisum**2)
##    
##
##    plt.plot(x , y, 'o', color = 'blue')
##    plt.plot(x, m*x + b, '-', color = 'green')
##
##    plt.ioff
##    plt.show()
##        
##        
##    
##
##    return (m, b)
##
##xval = np.array([1,2,3,4,5,6,7,8,9])
##yval = np.array([1,5,23,13,25,567,3,5,923])
##leastSquaresFitting(xval, yval)

#4-8


    
def distance(vect1, vect2):
    return (((vect1[0]-vect2[0])**2 + (vect1[1]-vect2[1])**2)**.5)

def planetSim():
    G = 1
    M = 1
    #planet 1
    rs0 = np.array([0,0])
    rp10 = np.array([-20,0])
    vp10 = np.array([0, .3])
    ap10 = ((-G*M)/(distance(rp10, rs0)**3))*rp10
    tp1=0
    rp1x = 0
    p1pos = []

    #planet2
    rp20 = np.array([-30,0])
    vp20 = np.array([0, .25])
    ap20 = ((-G*M)/(distance(rp10, rs0)**3))*rp10
    plt.plot(rs0[0], rs0[1], 'o', color = 'yellow')
    tp2=0
    rp2x = 0
    p2pos = []

    delT = .5
    times = np.arange(0,2500, 1)
    for t in times:
        #planet1
        plt.plot(rp10[0], rp10[1], 'o', color = 'red')
        rp11 = rp10 + vp10*delT + .5*ap10*(delT**2)
        ap11 = (-G*M/(distance(rp11, rs0)**3))*rp11
        vp11 = vp10 + .5*(ap11 + ap10)*delT
        rp10 = rp11
        ap10 = ap11
        vp10 = vp11
        p1pos.append(rp10)
        if rp10[0] > rp1x:
            rp1x = rp10[0]
            tp1 += 1
            
        

        #planet2
        plt.plot(rp20[0], rp20[1], 'o', color = 'blue')
        rp21 = rp20 + vp20*delT + .5*ap20*(delT**2)
        ap21 = (-G*M/(distance(rp21, rs0)**3))*rp21
        vp21 = vp20 + .5*(ap21 + ap20)*delT
        rp20 = rp21
        ap20 = ap21
        vp20 = vp21
        p2pos.append(rp20)
        if rp20[0] > rp2x:
            rp2x = rp20[0]
            tp2 += 1
        


        plt.axis('equal')
        plt.pause(.00001)
        

    ap1 = (rp1x + 20)/2
    ap2 = (rp2x + 30)/2
    tp1 = 2 * delT * tp1
    tp2 = 2 * delT * tp2
    print('planet1 a: ',ap1, ' t: ', tp1, 't^2/a^3 = ', tp1**2/ap1**3)
    print('planet2 a: ',ap2, ' t: ', tp2, 't^2/a^3 = ', tp2**2/ap2**3)
    plt.ioff()
    plt.show()

planetSim()


        
        
        
    
    
    
    
    


        
    
