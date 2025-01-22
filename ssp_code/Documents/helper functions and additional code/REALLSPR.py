from math import*
import numpy as np
import matplotlib.pyplot as plt

def RAdecToHMS(RA):
    hours = int(RA/15)
    minutes = int((RA-hours*15)/.25)
    seconds = (RA-hours*15-minutes*.25)*240
    return(hours, minutes, seconds)

def DECdecToDMS(dec):
    degSign = copysign(1, dec)
    if degSign < 0:
        deg = float(ceil(dec))
        minutes = float(ceil((dec-deg)*60))
    else:
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

def DMStoDeg(degrees, arcmin, arcsec):
    pos = copysign(1,degrees)
    bos = copysign(1,arcmin)
    if pos >= 1 and bos >= 0:
        deg = degrees + arcmin/60 + arcsec/3600
        #deg %= 360
        return (deg)
        
    elif(pos <= 1 and bos >= 1):
        deg = degrees - arcmin/60 - arcsec/3600
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
        

    return (m, b)

def spliceColumn(coef, const, j):
    coefficient = np.copy(coef)
    coefficient[:,j] = const
    return coefficient

def det3x3 (m):
    v1 = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
    v2 = m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])
    v3 = m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])

    return v1 - v2 + v3

#Least Square Wed
def LSPR(raS, decS, xS, yS, xa, ya):
    # Set initial value for sums
    ai = 0
    aixi = 0
    aiyi = 0

    di = 0
    dixi = 0
    diyi = 0
    
    xi = 0
    yi = 0
    xi2 = 0
    yi2 = 0
    xiyi = 0
    N = raS.size

    #Sum up values
    for i in range (raS.size):
        ai += raS[i]
        aiyi += raS[i] * yS[i]
        aixi += raS[i] * xS[i]
        xi += xS[i]
        yi += yS[i]
        xi2 += xS[i]**2
        yi2 += yS[i]**2
        xiyi += xS[i]*yS[i]

        di += decS[i]
        dixi += decS[i] * xS[i]
        diyi += decS[i] * yS[i]
        
        
    # Arrays for cramer
    coef1 = np.array([[N, xi, yi], [xi, xi2, xiyi],[yi, xiyi, yi2]])
    
    const = np.array([ai, aixi, aiyi])
    const2 = np.array([di, dixi, diyi])

    #Cramer
    d1 = spliceColumn(coef1, const, 0)
    d2 = spliceColumn(coef1, const, 1)
    d3 = spliceColumn(coef1, const, 2)

    d4 = spliceColumn(coef1, const2, 0)
    d5 = spliceColumn(coef1, const2, 1)
    d6 = spliceColumn(coef1, const2, 2)

    coef1 = det3x3(coef1)
    
    b1 = det3x3(d1)/coef1
    a11 = det3x3(d2)/coef1
    a12 = det3x3(d3)/coef1

    b2 = det3x3(d4)/coef1
    a21 = det3x3(d5)/coef1
    a22 = det3x3(d6)/coef1

    #RA and Dec Calc of Asteroid
    raAsteroid = b1 + a11 * xa + a12*ya
    decAsteroid = b2 + a21*xa + a22*ya

    #Residuals
    resia = np.array([])
    resid = np.array([])
    a = 0
    d = 0
    for j in range (raS.size):
        tempra = raS[j] - (b1 + a11 * xS[j] + a12 * yS[j])
        tempid = decS[j] - (b2 + a21 * xS[j] + a22 * yS[j])
        a+= tempra**2
        d += tempid**2
        resia = np.append(resia, tempra)
        resid = np.append(resid, tempid)
    

    sda = (a / (N-3))**.5
    sdd = (d / (N-3))**.5
    
    return(raAsteroid, decAsteroid, sda, sdd, resia, resid)

#make numbers decimals
def toDec(rh, rm,rs, dd, dm, ds):
    raDecs= np.array([])
    decDecs = np.array([])
    for i in range (rh.size):
        raDecs = np.append(raDecs, HMStoDeg(rh[i], rm[i], rs[i], False))
        decDecs = np.append(decDecs, DMStoDeg(dd[i], dm[i], ds[i]))
    return(raDecs, decDecs)

def animate(sRas, sDecs, aRas, aDec, sdRa, sdDec, mag):
    plt.scatter(aRas, aDec, c = 'red', s = (sdRa**2 + sdDec**2)*5000**2)
    for i in range(sRas.size):    
        plt.scatter(sRas[i], sDecs[i], s = mag[i]**2.7)

    plt.show()



#data reader
data = np.loadtxt('/home/chuang/LSPRdata.csv', dtype=float,delimiter=',')

dr, dc = data.shape
astX = data[dr-1,0]
astY = data[dr-1,1]
data = data[0:dr-1, 0:dc]

x = data[:,0]
y = data[:,1]
raHr = data[:,2]
raMin = data[:,3]
raSec = data[:,4]
decDeg = data[:,5]
decMin = data[:,6]
decSec = data[:,7]
mag = data[:, 8]


#testing

starRas, starDecs = toDec(raHr, raMin, raSec, decDeg, decMin, decSec)
rightAssAst, DecAst, sdra, sddec, residualRa, residualId = LSPR(starRas, starDecs, x, y, astX, astY)


print('RA: ', RAdecToHMS(rightAssAst), ' Residual: ', residualRa*3600, ' Standard Dev: ', sdra*3600)
print('Dec: ', DECdecToDMS(DecAst), ' Residual: ', residualId*3600 , ' Standard Dev: ', sddec * 3600) 

#print('Dec Test of -183.2412', DECdecToDMS(-183.2412))

animate(starRas, starDecs, rightAssAst, DecAst, sdra, sddec, mag)


    



