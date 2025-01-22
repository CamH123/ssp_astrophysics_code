from math import*
import numpy as np
import matplotlib.pyplot as plt

#ps2-6-C
def DECdecToDMS(dec):
    deg = float(round(dec))
    print('deg is' , deg)
    pos = copysign(1, dec)
    minutes = float(round((dec-deg)*60))
    print('min is ' , minutes)
    seconds = float(((dec-deg-(minutes/60))*3600))
    print('sec is ' , seconds)
    if deg == 0 and (minutes <0 or seconds < 0):
        deg = -0.0
    minutes = abs(minutes)
    seconds = abs(seconds)
    return(deg, int(minutes), seconds)

#ps2-6-A
def DMStoDeg(degrees, arcmin, arcsec):
    pos = copysign(1,degrees)
    bos = copysign(1,arcmin)
    if pos >= 1 and bos >= 1:
        deg = degrees + arcmin/60 + arcsec/3600

        return (deg)
        
    elif(pos < 1 and bos >= 1):
        deg = degrees - arcmin/60 - arcsec/3600

        return (deg)
    elif (pos <1 and bos <1):
        deg = degrees + arcmin/60 + arcsec/3600

        return (deg)
        
    else:
        deg = degrees - arcmin/60 - arcsec/3600

        return (deg)
#dms to dms
print(DMStoDeg(-18, 15, 27.4))
print(DECdecToDMS(-18.25761111111111))
print(' ')

### deg to deg 
##print(DECdecToDMS(-34.0))
##print(DMStoDeg(-34, 0, 0))




####def DMStoDeg(degrees, arcmin, arcsec):
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



##def DECdecToDMS(dec):
##    deg = float(round(dec))
##    pos = copysign(1, dec)
##    minutes = float(round((dec-deg)*60))
##    seconds = float(round(((dec-deg-minutes/60)*3600)))
##    if minutes < 0:
##        return(deg*-1, minutes*-1, seconds)
##    return(deg, minutes, seconds)
####
