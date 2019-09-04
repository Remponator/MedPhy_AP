import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 

#C Wert 3
L2 = ufloat(20.1*10**(-3),0.002*20.1*10**(-3))
R2 = ufloat(79, 79*0.002)
R3 = 571
R4 = 429

X = ufloat(R3/R4, (R3/R4)*0.005)    #R3/R4

Rx = R2*X
Lx = L2*X

print('Rx: ', "{:.3f}".format(Rx))
print('Lx: ', "{:.6f}".format(Lx))