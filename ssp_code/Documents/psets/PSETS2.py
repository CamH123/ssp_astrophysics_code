from math import*
import numpy as np
import matplotlib.pyplot as plt

###PS2-4
##def integ (integrand, lowlim, uplim, N):
##    tot = 0.0
##    step = (uplim-lowlim)/(N)
##    for x in np.arange(lowlim + step/2, uplim + step/2, step):
##        tot += step*integrand(x)
##    return tot
##
###print (integ(np.sin(x), -5, 5, 1000))
##
###PS3-5 Angle units conversion
##def quadcheck(so, co):
##    if (so >= 0 and co >= 0):
##        print("1")
##        return np.arccos(co)
##        
##    elif(so > 0 and co < 0):
##        print("2")
##        return np.arccos(co)
##        
##    elif(so < 0 and co < 0):
##        print("3")
##        return 2*pi - np.arccos(co)
##        
##    else:
##        print("4")
##        return 2*pi - np.arccos(co)
##        
##        
###print(quadcheck(cos(241*pi/27), sin(241*pi/27)))
##
###ps2-6-A
##def DMStoDeg(degrees, arcmin, arcsec):
##    pos = copysign(1,degrees)
##    bos = copysign(1,arcmin)
##    if pos >= 1 and bos >= 0:
##        deg = degrees + arcmin/60 + arcsec/3600
##        #deg %= 360
##        return (deg)
##        
##    elif(pos <= 1 and bos >= 1):
##        deg = degrees - arcmin/60 + arcsec/3600
##        #deg %= 360
##        return (deg)
##    elif (pos <=1 and bos <=1):
##        deg = degrees + arcmin/60 + arcsec/3600
##        #deg %= 360
##        return (deg)
##        
##    else:
##        deg = degrees - arcmin/60 - arcsec/3600
##        #deg %= 360
##        return (deg)
##
##
##
###ps2-6-B
##def RAdecToHMS(RA):
##    hours = int(RA/15)
##    minutes = int((RA-hours*15)/.25)
##    seconds = int((RA-hours*15-minutes*.25)*240)
##    return(hours, minutes, seconds)
##    
##
##
###ps2-6-C
##def DECdecToDMS(dec):
##    deg = float(round(dec))
##    print('deg is' , deg)
##    pos = copysign(1, dec)
##    minutes = float(round((dec-deg)*60))
##    print('min is ' , minutes)
##    seconds = float(((dec-deg-(minutes/60))*3600))
##    print('sec is ' , seconds)
##    if deg == 0 and (minutes <0 or seconds < 0):
##        deg = -0.0
##    minutes = abs(minutes)
##    seconds = abs(seconds)
##    return(deg, int(minutes), seconds)
##
###PS2-6-D
##def mag(vect):
##    return((vect[0]**2 + vect[1]**2 + vect[2]**2)**.5)
##
###TESTER
##def HMStoDeg(hours, minutes, seconds, dOr):
##
##    deg = (hours/24)*360 + (minutes/(24*60))*360 + (seconds/(24*3600))*360
##    deg %= 360
##    if dOr == False:
##        return (deg)
##    else:
##        return (deg * pi /180)
##
###PS2-7-C
##def rotMatrix(vect1, a, b):
##    x = vect1[0]
##    y = vect1[1]
##    z = vect1[2]
##    rot1 = np.array([[cos(a), sin(a), 0], [-1*sin(a), cos(a), 0], [0, 0, 1]])
##    rot2 = np.array([[1, 0, 0], [0, cos(b), sin(b)], [0, -1*sin(b), cos(b)]])
##    finRot = np.matmul(rot2,rot1)
##    finvect = np.matmul(finRot,vect1)
##    return finvect
##
###PS2-8-A
##hyp = np.array([])
##x = np.array([])
##y = 0
##for i in np.arange(-10*pi, 10*pi, .01):
##    hyp = np.append(hyp, [y])
##    x = np.append(x, i)
##    y+=1
##
##x1 = hyp*np.cos(x)
##y1 = hyp*np.sin(x)
##plt.plot(x1, y1, 'r-')
##plt.axis('equal')
##plt.show()

#PS2-8-B
t = np.arange(-10*pi, 10*pi, .5)
x2 = 15*np.sin(t)**3
y2 = 11*np.cos(t)

plt.plot(x2, y2, 'r-')
plt.axis('equal')
plt.show()
    
    

      
    
            

    
    
    


