from math import*
import numpy as np
import matplotlib.pyplot as plt

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
def AltAztoRaDec(azi, alt, lst):
    lat = 40*pi/180
    azi*=pi/180
    alt*=pi/180
##    if azi < 180:
##        alt *= -1
    dec = np.arcsin(np.sin(lat)*np.sin(alt)+np.cos(lat)*np.cos(alt)*np.cos(2*pi-azi))
    
    cosHA = (np.sin(alt)-np.sin(dec)*np.sin(lat))/(np.cos(dec)*np.cos(lat))
    if cosHA < -1 or cosHA > 1:
        cosHA = round(cosHA)
    sinHA = -1*np.sin(azi)*np.cos(alt)/np.cos(dec)
    ha = quadcheck(sinHA,cosHA)
    decLst = HMStoDeg(lst[0], lst[1], lst[2], False)
    ha *= 180/pi
    ra = decLst-ha
    dec*= 180/pi
    ra%=360
    return(ra, dec)

r = np.array([0, 0, 0])
print(AltAztoRaDec(0, 0, r))
print('quad', quadcheck(-1, 0))
