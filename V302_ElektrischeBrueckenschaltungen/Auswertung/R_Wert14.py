import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 

#R Wert 13
R20 = np.array([332,664,1000])
R3= np.array([728,571,468])
R4 = np.array([272,429,532])

R2 = unp.uarray(R20, 0.002*R20)
X = unp.uarray(R3/R4, (R3/R4)*0.005)    #R3/R4

Rx = R2*X

M = np.mean(Rx) #Mittelwert
V = np.var(Rx)  #Fehler des Mittelwerts
F = V**(0.5)/3**(0.5)

print('Mittelwert:',"{:.5f}".format(M))
print('Fehler des Mittelwerts:',"{:.5f}".format(F))