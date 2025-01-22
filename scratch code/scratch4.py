from math import*
import numpy as np
import matplotlib.pyplot as plt

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
    p1posx = []
    p1posy = []
    min1 = False
    max1 = False
    rp1min = 20
    rp1max = 0
    tmina1 = 0
    tmaxa1 = 0


    #planet2
    rp20 = np.array([-30,0])
    vp20 = np.array([0, 0.25])
    ap20 = ((-G*M)/(distance(rp10, rs0)**3))*rp10
    plt.plot(rs0[0], rs0[1], 'o', color = 'yellow')
    tp2=0
    rp2x = 0
    p2posx = []
    p2posy = []
    min2 = False
    max2 = False
    rp2min = 30
    rp2max = 0
    tmin2 = 0
    tminb1 = 0
    tmaxb1 = 0

    times = np.arange(0,200000, 1)
    delT = 1
    for t in times:

        
        #planet1
        #plt.plot(rp10[0], rp10[1], 'o', color = 'red')
        rp11 = rp10 + vp10*delT + .5*ap10*(delT**2)
        ap11 = (-G*M/(distance(rp11, rs0)**3))*rp11
        vp11 = vp10 + .5*(ap11 + ap10)*delT
        rp10 = rp11
        ap10 = ap11
        vp10 = vp11
        p1posx.append(rp10[0])
        p1posy.append(rp10[1])
        if distance(rp10, rs0) > rp1max:
            rp1max = distance(rp10, rs0)
            tp1+=1
            

            
        if distance(rp10, rs0) < rp1min:
            rp1min = distance(rp10, rs0)


##        if distance(rp10, rs0) < rp1max and min1 == False:
##            tmina1 = t
##            min1 = True
##            
##            
##
##        if rp10[0] < -20 and max1 == False and min1 == True:
##
##            tmaxa1 = t
##            max1 = True
##            break


            
            
        

        #planet2
        #plt.plot(rp20[0], rp20[1], 'o', color = 'blue')
        rp21 = rp20 + vp20*delT + .5*ap20*(delT**2)
        ap21 = (-G*M/(distance(rp21, rs0)**3))*rp21
        vp21 = vp20 + .5*(ap21 + ap20)*delT
        rp20 = rp21
        ap20 = ap21
        vp20 = vp21
        p2posx.append(rp20[0])
        p2posy.append(rp20[1])
        if distance(rp20, rs0) > rp2max:
            rp2max = distance(rp20, rs0)
            tp2 +=1
        if distance(rp20, rs0) < rp2min:
            rp2min = distance(rp20, rs0)

##        if distance(rp20, rs0) < rp2max and min2 == False:
##            tminb2 = t
##            min2 = True
##
##        if distance(rp20, rs0) > rp2min and max2 == False:
##            tmaxb2 = t
##            max2 = True
            


##        plt.axis('equal')
##        plt.pause(.01)
        
    print(tmina1)
    print(tmaxa1)
    ap1 = (rp1max + rp1min)/2
    ap2 = (rp2max + rp2min)/2
    tp1 = 2 * delT * tp1
    tp2 = 2 * delT * tp2
    plt.plot(p1posx, p1posy, '-', color = 'red')
    plt.plot(p2posx, p2posy, '-', color = 'blue')
    plt.axis('equal')
    plt.pause(.1)
    print('planet1 a: ',ap1, ' t: ', tp1, 't^2/a^3 = ', (tp1**2)/(ap1**3))
    print('planet2 a: ',ap2, ' t: ', tp2, 't^2/a^3 = ', (tp2**2)/(ap2**3))
    print(tp1)
    plt.ioff()
    plt.show()

planetSim()

