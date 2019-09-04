import numpy as np 
import scipy.constants as const
import math

h = 0.028

r = 0.0165

a = np.array([0.28,0.26,0.24,0.22,0.20,0.18,0.16,0.14,0.12,0.10]) - r

T = np.array([6.72,6.16,5.87,5.28,4.72,4.14,3.82,3.60,3.01,3.09])

M = 0.2229

m = 595

b = 3.225

mD, fmD = np.genfromtxt('/Users/Remponator/Desktop/Praktikum/V101 - Trägheitsmoment/Auswertung/Winkelgröße D', unpack=True)

def I(mD,T):
    return np.array(((T**2)*mD)/4*(math.pi**2))

def dI(mD,fmD,T):
    return np.sqrt(((T**2)/(4*(math.pi)**2)*fmD)**2)

def mI(I):
    return np.mean(I(mD,T))

def mdI(dI):
    return np.mean(dI(mD,fmD,T))

def Id(mD,m,r,h,M):
    return ((b*mD)/(4*((math.pi)**2))-2*M*(((r**2)/4)+((h**2)/(12))))

def dId(fmD,b):
    return np.sqrt(((b/(4*(math.pi**2)))*fmD)**2)

#def x(a):
 #   return np.array(a-np.mean(a))

#def y(I,mI):
  #  return np.array(I(mD,T)-mI(I))

#def ai(b,mI,a):
 #   return (mI(I)-b(x,y)*np.mean(a))

#print(a)
#print(mD)
#print(I(mD,T))
#print(dI(mD,fmD,T))
#print(mI(I))
#print(mdI(dI))
#print(np.mean(a))
#print(x(a))
#print(y(I,mI))
#print(b(x,y))
#print(ai(b,mI,a))
print(Id(mD,m,r,h,M))
print(dId(fmD,b))