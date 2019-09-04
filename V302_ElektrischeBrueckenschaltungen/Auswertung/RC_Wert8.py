import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 

#C Wert 3
C20 = np.array([399*10**(-9), 450*10**(-9), 750*10**(-9)])
R20 = np.array([426,378,229])
R3= np.array([573,601,714])
R4 = np.array([427,399,286])

C2 = unp.uarray(C20, 0.002*C20)
R2 = unp.uarray(R20,0.002*R20)
X1 = unp.uarray(R3/R4, (R3/R4)*0.005)    #R3/R4
X2 = unp.uarray(R4/R3, (R4/R3)*0.005)    #R4/R3

Rx = R2*X1
Cx = C2*X2

M1 = np.mean(Rx) #Mittelwert
V1 = np.var(Rx)  #Fehler des Mittelwerts
F1 = V1**(0.5)/3**(0.5)

print('Mittelwert Rx: ', "{:.3f}".format(M1))
print('Fehler des Mittelwerts Rx: ', "{:.3f}".format(F1))

M2 = np.mean(Cx) #Mittelwert
V2 = np.var(Cx)  #Fehler des Mittelwerts
F2 = V2**(0.5)/3**(0.5)

print('Mittelwert Cx: ', "{:.12f}".format(M2))
print('Fehler des Mittelwerts Cx: ', "{:.12f}".format(F2))