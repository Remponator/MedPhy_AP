from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

t,TC,rho = np.loadtxt("/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V207-DasKugelfall-ViskosimeterNachHoeppler-/Auswertung/t3.txt", unpack=True)

T = TC + 273.15
K_gr = 9.543*(10**-9)
rho_gr = 2595.344

def mu(K_gr, rho, rho_gr,t):
    return K_gr*(rho_gr-rho)*t

def y(mu):
    return np.log(mu(K_gr, rho, rho_gr,t))

x = 1/T
plt.plot(x,y(mu),'bx',label = r'Messwerte')

def f(A,B,x):
    return A*x+B

params, covariance = curve_fit(f,x,y(mu))
errors = np.diag(covariance)

print('A:', params[0], '+-', errors[0])
print('B:', params[1], '+-', errors[1])

plt.plot(x, f(x, *params), 'r-', label = r'Ausgleichsgerade') 
plt.grid()
plt.xlabel(r'$\frac{1}{T}$' r'/ $\frac{1}{K}$')
plt.ylabel('$\t{ln}(\eta\cdot\t{Pa}^{-1}\t{s}^{-1})$')
plt.legend()
plt.show()
#print(x(mu))

#print("mu =",mu(K_gr, rho, rho_gr,t))