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
x, y = np.loadtxt("/home/jones/Documents/Praktikum/V303 Lock-In Verstärker//Tabelle2.txt", unpack=True)

X = math.pi*x/200
Y = y/1000
xdata = np.linspace(0, 6, 100)
plt.plot(X,Y,'rx')

def f (X,w,A,C,E):
    return A*np.sin(w*X+E) + C

params, covariance = curve_fit(f, X, Y)
errors = np.diag(covariance)

print('w:', params[0], '+-', errors[0])
print('A:', params[1], '+-', errors[1])
print('C:', params[2], '+-', errors[2])
print('E:', params[3], '+-', errors[3])

plt.plot(X, f(X, *params), 'r-', label = r'Ausgleichsgerade') 
plt.grid()
plt.xlabel('$Phi$ / $rad$')
plt.ylabel('$U$ / $V$')
plt.savefig('Sinus2.pdf')