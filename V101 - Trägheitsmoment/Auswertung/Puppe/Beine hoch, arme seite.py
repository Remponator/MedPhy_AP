import numpy as np 
import scipy.constants as const
import math

T = np.array([0.77,0.63,0.73,0.8,0.73])

def mT(T):
    return np.mean(T)

def dmT(T):
    return np.std(T)/np.sqrt(len(T))


print(mT(T))
print(dmT(T))