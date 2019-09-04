from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants.constants as const
from uncertainties import ufloat
from uncertainties import unumpy
import math

# Messdaten
r,U  = np.loadtxt("/home/jones/Documents/Praktikum/V303 Lock-In Verstärker/led1.txt", unpack=True)
plt.plot(r,U,'rx',label = r'Messwerte')

def f (r,a,b):
    return a/r**2+b

params, covariance = curve_fit(f, r, U)
errors = np.diag(covariance)

print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])

plt.plot(r, f(r, *params), 'b-', label = r'Ausgleichskurve') 

plt.xlabel('$a$ / $cm$')
plt.ylabel('$U$ / $V$')
plt.grid()
plt.legend()
plt.show()