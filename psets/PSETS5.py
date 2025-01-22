from math import*
import numpy as np
import matplotlib.pyplot as plt

###PSET4
###PS5-5
##def NewtonRaphson(f, deri, intGuess, error ):
##    xi = intGuess
##    while (f(xi) > error or f(xi) < -error):
##        xi = intGuess
##        xi2 = xi - (f(xi)/deri(xi))
##    return(xi)
##
##
##    
##
##
##NewtonRaphson(3*pi/4, .41)

###PS5-10 3 body sim
##
##def distance(vect1, vect2):
##    return (((vect1[0]-vect2[0])**2 + (vect1[1]-vect2[1])**2)**.5)
##
##def threeBodySim():
##    G = 1
##    Msun = 100
##    Mearth = 2
##    Mmoon = .1
##
##    #Sun
##    rs0 = np.array([0,0])
##    vs0 = np.array([0,0])
##    as0 = np.array([0,0])
##    sunPos = []
##
##
##    
##    #Earth
##    re0 = np.array([40,0])
##    ve0 = np.array([0,1.6])
##    ae0 = np.array([0,0])
##    earthPos = []
##    
##    #Moon
##    rm0 = np.array([42,0])
##    vm0 = np.array([0,2.6])
##    am0 = np.array([0,0])
##    moonPos = []
##
##    times = np.arange(0,100000, 1)
##    delT = .1
##    k = 0
##    j = 0
##    for t in times:
####        #Sun
####        plt.plot(rs0[0], rs0[1], 'o', color = 'yellow')
####        rs1 = rs0 + vs0 * delT + .5*as0*(delT**2)
####        as1 = (((-G*Mearth)/(distance(rs1, re0)**3)) + ((-G*Mmoon)/(distance(rs1, rm0)**3)))*rs1
####        #as1 = ((-G*Mmoon)/(distance(rs1, rm0)**3))*rs1
####        vs1 = vs0 + .5*(as0 + as1)*delT
####        rs0 = rs1
####        as0 = as1
####        vs0 = vs1
####
####        #Earth
####        plt.plot(re0[0], re0[1], 'o', color = 'blue')
####        re1 = re0 + ve0 * delT + .5*ae0*(delT**2)
####        ae1 = (((-G*Msun)/(distance(re1, rs0)**3)) + ((-G*Mmoon)/(distance(re1, rm0)**3)))*re1
####        #ae1 = ((-G*Mmoon)/(distance(re1, rm0)**3))*re1
####        ve1 = ve0 + .5*(ae0 + ae1)*delT
####        re0 = re1
####        ae0 = ae1
####        ve0 = ve1
####
####        #Moon
##
##
##
##
##
##        
####        plt.plot(rm0[0], rm0[1], 'o', color = 'red')
####        rm1 = rm0 + vm0 * delT + .5*am0*(delT**2)
####        am1 = (((-G*Msun)/(distance(rm1, rs0)**3)) + ((-G*Mearth)/(distance(rm1, re0)**3)))*rm1
####        #am1 = ((-G*Mearth)/(distance(rm1, re0)**3))*rm1
####        vm1 = vm0 + .5*(am0 + am1)*delT
####        rm0 = rm1
####        am0 = am1
####        vm0 = vm1
##        k += 1
##        j += 1
##        if k % 10 == 0:
##            plt.plot(rs0[0], rs0[1], 'o', color = 'yellow')
##            plt.plot(re0[0], re0[1], 'o', color = 'blue')
##            plt.plot(rm0[0], rm0[1], 'o', color = 'red')
##        if j % 300 == 2:
##            print(Ugse + Ugme + Ugms + Kes + Kee + Kem)
##        
##        rs1 = rs0 + vs0 * delT + .5*as0*(delT**2)
##        re1 = re0 + ve0 * delT + .5*ae0*(delT**2)
##        rm1 = rm0 + vm0 * delT + .5*am0*(delT**2)
##        
##        as1 = ((-G*Mearth)/(distance(rs1, re0)**3)) * (rs1 - re0) + ((-G*Mmoon)/(distance(rs1, rm0)**3)) * (rs1 - rm0)
##        ae1 = ((-G*Msun)/(distance(re1, rs0)**3)) * (re1 - rs0) + ((-G*Mmoon)/(distance(re1, rm0)**3)) * (re1 - rm0)
##        am1 = ((-G*Msun)/(distance(rm1, rs0)**3)) * (rm1 - rs0) + ((-G*Mearth)/(distance(rm1, re0)**3)) * (rm1 - re0)
##
##        vs1 = vs0 + .5*(as0 + as1)*delT
##        ve1 = ve0 + .5*(ae0 + ae1)*delT
##        vm1 = vm0 + .5*(am0 + am1)*delT
##
##        
##        
##        
##        rs0 = rs1
##        as0 = as1
##        vs0 = vs1
##        
##        re0 = re1
##        ae0 = ae1
##        ve0 = ve1
##
##        rm0 = rm1
##        am0 = am1
##        vm0 = vm1
##
##        plt.axis('equal')
##        plt.pause(.001)
##
##        Ugse = -G * Msun * Mearth / distance(rs1, re1)
##        #Uges = -G * Msun * Mearth / distance(re1, rs1)
##        Ugme = -G * Mmoon * Mearth / distance(rm1, re1)
##        #Ugem = -G * Mmoon * Mearth / distance(re1, rm1) 
##        Ugms = -G * Msun * Mmoon / distance(rs1, rm1)
##        #Ugsm = -G * Msun * Mmoon / distance(rm1, rs1)
##        
##
##        Kes = .5 * Msun * (vs1[0]**2 + vs1[1]**2)
##        Kee = .5 * Mearth * (ve1[0]**2 + ve1[1]**2)
##        Kem = .5 * Mmoon * (vm1[0]**2 + vm1[1]**2)
##
##        
##        
##        #print(Ugse + Uges + Ugme + Ugem + Ugms + Ugsm + Kes + Kee + Kem)
##    plt.ioff()
##    plt.show()
##
##threeBodySim()

        
        
        



#11 Taylor Series
def taylorSin(x, N):
    f = 0
    for i in range(N):
        f += (((-1)**(i))*x**(2*i+1))/(factorial(2*i + 1))

    return f

def plotSin(n1, n2, n3):
    times = np.arange(0,100,.01)
    yn1 = np.array([])
    yn2 = np.array([])
    yn3 = np.array([])
    for i in times:
        yn1 = np.append(yn1, taylorSin(i, n1))
        yn2 = np.append(yn2, taylorSin(i, n2))
        yn3 = np.append(yn3, taylorSin(i, n3))

    plt.plot(times, yn1, '-', color = 'red')
    plt.plot(times, yn2, '-', color = 'blue')
    plt.plot(times, yn3, '-', color = 'green')
    plt.ylim(-1,1)
    plt.xlim(-1,51)

    plt.show()
    print('N reaches an internal limit at 77 and x at 37')
    
        
    
plotSin(5,20, 48)
    
