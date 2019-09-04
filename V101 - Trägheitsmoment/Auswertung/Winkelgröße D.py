import numpy as np 
import scipy.constants as const
import math

phig = np.array([60,90,120,160,180,200,220,240,260,280])

phi = phig * (math.pi/180)

F = np.array([0.02,0.04,0.12,0.18,0.21,0.25,0.28,0.32,0.34,0.40])

a = 0.25

def D(phi,F,a):
    return np.array((F*a)/phi)

def mD(D):
    return np.mean(D(phi,F,a))

def sD(D):
    return np.std(D(phi,F,a))

def fmD(sD,F):
    return sD(D)/(np.sqrt(len(F)))

np.savetxt('/Users/Remponator/Desktop/Praktikum/V101 - Trägheitsmoment/Auswertung/Winkelgröße D', [mD(D),fmD(sD,F)])
    
print(D(phi,F,a))
print(mD(D))
print(sD(D))
print(fmD(sD,F))