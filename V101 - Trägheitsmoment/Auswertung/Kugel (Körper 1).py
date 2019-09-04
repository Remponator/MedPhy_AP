import numpy as np 
import scipy.constants as const
import math

r = 0.0675

phig = 60
phi = phig * (math.pi/180)

M = 0.8123

T = np.array([1.36,1.43,1.33,1.38,1.33])

def mT(T):
    return np.mean(T)

def dmT(T):
    return np.std(T)/np.sqrt(len(T))



print(mT(T))
print(dmT(T))
