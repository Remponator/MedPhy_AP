import numpy as np 
import scipy.constants as const
import math

T = np.array([0.9,1.07,0.94,0.83,0.8])

r = 0.079/2

h = 0.138

M = 1.5663

def mT(T):
    return np.mean(T)

def dmT(T):
    return np.std(T)/np.sqrt(len(T))


print(mT(T))
print(dmT(T))
