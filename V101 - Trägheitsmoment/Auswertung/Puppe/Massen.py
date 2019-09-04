import numpy as np 
import scipy.constants as const
import math

Mg = 0.1624

R = np.array([0.0133,0.0171,0.0069,0.0075])

dR = np.array([0.0006,0.0015,0.0004,0.0007])

Vt = np.array([2.779,8.635,2.004,2.615])*(10**(-5))

dVt = np.array([0.251,1.515,0.232,0.488])*(10**(-5))

Vg = 20.652*(10**(-5))

dVg = 3.206*(10**(-5))

def Mt(Mg,Vt,Vg):
    return (Vt/Vg)*Mg

def dMt(Mg,Vt,dVt,Vg,dVg):
    return np.sqrt((((1/Vg)*Mg*dVt)**2)+((-Vt/(Vg**2))*Mg*dVg)**2)

def dI1(Mt,R,dR):
    return np.sqrt(((Mt(Mg,Vt,Vg)*R*dR)**2)+(((R**2)/2)*dMt(Mg,Vt,dVt,Vg,dVg))**2)

dIA = np.sqrt((((((0.0069**2)/4)+((0.134**2)/12)+0.0841**2)*0.0031)**2)+(((0.0158*0.0069)/2)*0.0004)**2)



print(Mt(Mg,Vt,Vg))
print(dMt(Mg,Vt,dVt,Vg,dVg))
print(dI1(Mt,R,dR))
print(dIA)