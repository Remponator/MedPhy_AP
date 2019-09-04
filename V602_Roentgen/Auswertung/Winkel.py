import numpy as np 

E = 13.47e3

def Teta(E):
    return np.arcsin(((6.626e-34)*3e8)/(2*(201.4e-12)*E*1.6e-19))

print(np.degrees(Teta(E)))