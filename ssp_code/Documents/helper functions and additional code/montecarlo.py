#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 10:23:53 2023

@author: chuang
"""

from math import*
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits



def montCarlo (fieldRA, indexRA, fieldDec, indexDec, objNum):
    sumRA = 0
    sumDec = 0
    for i in range(objNum):
        sumRA += (fieldRA[i] - indexRA[i])**2
        sumDec+= (fieldDec[i] - indexDec[i])**2
    sdRA = (sumRA/objNum)**.5
    sdDec = (sumDec/objNum)**.5
    
    return sdRA, sdDec
        
table = fits.open('/home/chuang/Downloads/corr.fits')[1].data

fieldRA = table.field_ra
indexRA = table.index_ra
fieldDec = table.field_dec
indexDec = table.index_dec


numObj = int(table.shape[0])
sdRA, sdDec = montCarlo(fieldRA, indexRA, fieldDec, indexDec, numObj)
print(sdRA, sdDec)
