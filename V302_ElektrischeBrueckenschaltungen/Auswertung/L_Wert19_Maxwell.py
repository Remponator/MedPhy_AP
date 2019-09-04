import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 

#C Wert 3
R2 = ufloat(664, 664*0.002)
R3 = ufloat(104, 104*0.03)
R4 = ufloat(604, 604*0.03)
C4 = ufloat(399*10**(-9) , 450*10**(-9)*0.002)

Rx = R2*R3/R4
Lx = R2*R3*C4

print('Rx: ', "{:.3f}".format(Rx))
print('Lx: ', "{:.12f}".format(Lx))