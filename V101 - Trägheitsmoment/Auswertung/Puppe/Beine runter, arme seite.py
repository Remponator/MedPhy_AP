import numpy as np 
import scipy.constants as const
import math

T = np.array([0.5,0.52,0.49,0.46,0.54])

def mT(T):
    return np.mean(T)

def dmT(T):
    return np.std(T)/np.sqrt(len(T))


print(mT(T))
print(dmT(T))