from math import*
import numpy as np
import matplotlib.pyplot as plt

##CODE FROM BEFORE TO HELP WITH UNITS CONVERSIONS
#PS3-5 Angle units conversion
def quadcheck(so, co):
    if (so >= 0 and co >= 0):
        return np.arccos(co)
        
    elif(so > 0 and co < 0):
        return np.arccos(co)
        
    elif(so < 0 and co < 0):
        return 2*pi - np.arccos(co)
        
    else:
        return 2*pi - np.arccos(co)

def DMStoDeg(degrees, arcmin, arcsec):
    pos = copysign(1,degrees)
    bos = copysign(1,arcmin)
    if pos >= 1 and bos >= 0:
        deg = degrees + arcmin/60 + arcsec/3600
        #deg %= 360
        return (deg)
        
    elif(pos <= 1 and bos >= 1):
        deg = degrees - arcmin/60 + arcsec/3600
        #deg %= 360
        return (deg)
    elif (pos <=1 and bos <=1):
        deg = degrees + arcmin/60 + arcsec/3600
        #deg %= 360
        return (deg)
        
    else:
        deg = degrees - arcmin/60 - arcsec/3600
        #deg %= 360
        return (deg)
    
def HMStoDeg(hours, minutes, seconds, dOr):

    deg = (hours/24)*360 + (minutes/(24*60))*360 + (seconds/(24*3600))*360
    deg %= 360
    if dOr == False:
        return (deg)
    else:
        return (deg * pi /180)

## PSET CODES

#HW3-4 Projectivle-Motion
###Part A
##def projmotA(vel, theta):
##    theta *= pi/180
##    v0x = vel*cos(theta)
##    v0y = vel*sin(theta)
##    delT = 0.005 
##    airTime = 2*v0y / 9.8
##    times = np.arange(0,airTime,delT)
##    plt.figure(figsize = (6,6))
##    x = 0
##    y = 0
##    for t in times:
##        x = v0x*t
##        y = v0y*t + .5*(-9.8)*t**2
##        plt.plot(x,y,'o',color ='red')
##        plt.ylim(-2, (v0y**2)/(2*9.8) + 10)
##        plt.xlim(-2, x + 10 )
##        plt.pause(0.01*delT)
##    plt.ioff()
##    plt.show() 
##    print('flight time: ' , airTime , ' range: ',(vel**2)*np.sin(2*theta)/9.8, x)
##
##projmotA(20, 60)

#Part B
def projmotB(vel, theta):
    #b = (1/2)*1*1.293 * ((.085**2)*pi)
    #m = .4
    b = 0.5*0.2*1.293*0.024
    m = 0.5
    theta *= pi/180
    v0x = vel*cos(theta)
    v0y = vel*sin(theta)
    v2x = v0x
    v2y = v0y
    v = (v0y**2 + v0x**2)**.5
    delT = 0.08
    times = np.arange(0,10,delT)
    plt.figure(figsize = (6,6))
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    t1 = 0
    t0 = 0
    while y2 >= 0:
        if y >=0:
            t0 += 1
            aX=(-b/m) * v * v0x
            aY = (-9.8-(b/m)*v*v0y)
            x1 = x + v0x*delT + .5*aX * delT**2
            y1 = y + v0y*delT + .5*aY * delT**2
            v1x = v0x + aX*delT
            v1y = v0y + aY*delT
            x = x1
            y = y1
            v0x = v1x
            v0y = v1y
            v = (v0y**2 + v0x**2)**.5
            plt.plot(x,y,'o',color ='red')
            plt.ylim(-2, y + 100)
            plt.xlim(-2, x2 + 10 )
            
        t1+=delT
        x2 = v2x*t1
        y2 = v2y*t1 + .5*(-9.8)*t1**2
        plt.plot(x2, y2, 'o', color = 'blue')
        plt.ylim(-2, y + 100)
        plt.xlim(-2, x2 + 10 )
        plt.pause(0.01*delT)

    #while y2 >= 0:

        
    print('with drag time is ', t0, ' and range is ', x)
    print('without drag time is ', t1, ' and range is ', x2)  
    plt.ioff()
    plt.show() 
   

##projmotB(42, 47)

#HW3-5 Fruit Ninja
fruits = np.array([["Apple","Banana","Blueberry","Cherry"],
["Coconut","Grapefruit","Kumquat","Mango"],
["Nectarine","Orange","Tangerine","Pomegranate"],
["Lemon","Raspberry","Strawberry","Tomato"]])

#a
bottomRight = fruits[3,3]
print(bottomRight)

#b
center = fruits[1:3, 1:3]
print(center)

#c
row13 = np.array([fruits[0,:],fruits[2,:]])
print(row13)

#d
centerRev = fruits[-2:0:-1, -2:0:-1]
print(centerRev)

#e

swap14 = np.copy([fruits[0:4,0]])
fruits[0:4,0] = fruits[0:4,3]
fruits[0:4,3] = swap14
print(fruits)

#f
fruits[:,:] = 'SLICED!'
print(fruits)
  


### 3-6 Alt-Az
##def AltAztoRaDec(azi, alt, lst):
##    lat = 40*pi/80
##    azi*=pi/180
##    alt*=pi/180
##    dec = np.arccos(np.sin(lat)*np.sin(alt)+np.cos(lat)*np.cos(alt)*np.cos(2*pi-azi))
##    dec*= 180/pi
##    cosHA = (np.sin(alt)-np.sin(dec)*np.sin(lat))/(np.cos(dec)*np.cos(lat))
##    sinHA = -1*np.sin(azi)*np.cos(alt)/np.cos(dec)
##    ha = quadcheck(cosHA,sinHA)
##    decLst = HMStoDeg(lst[0], lst[1], lst[2], False)
##    ha *= 180/pi
##    ra = decLst-ha
##    return(ra, dec)
##    
##r = np.array([20, 13, 33])
##print(AltAztoRaDec(20, 20, r))
