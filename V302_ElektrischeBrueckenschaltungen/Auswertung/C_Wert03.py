import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 

#C Wert 3
C20 = np.array([399*10**(-9), 450*10**(-9), 750*10**(-9)])
R3= np.array([485,513,636])
R4 = np.array([515,487,364])

C2 = unp.uarray(C20, 0.002*C20)
X = unp.uarray(R4/R3, (R4/R3)*0.005)    #R4/R3

Cx = C2*X

M = np.mean(Cx) #Mittelwert
V = np.var(Cx)  #Fehler des Mittelwerts
F = V**(0.5)/3**(0.5)

print('Mittelwert Cx: ', "{:.12f}".format(M))
print('Fehler des Mittelwerts Cx: ', "{:.12f}".format(F))