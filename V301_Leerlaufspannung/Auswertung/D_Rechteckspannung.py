import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

U = np.array([0.175,0.21,0.25,0.275,0.28,0.31,0.33,0.36,0.38,0.39])

I = np.array([0.007,0.0062,0.0055,0.0052,0.0046,0.0041,0.0037,0.0033,0.0030,0.0026])

def f(m,I,b):
    return m*I+b

params, covariance = curve_fit(f, I, U)
errors = np.diag(covariance)

print('Ri:', params[0], '+-', errors[0])
print('U0:', params[1], '+-', errors[1])

plt.plot(I, f(I, *params), 'r-', label = r'Ausgleichsgerade')

plt.plot(I, U, 'x', label=r'Messdaten')

plt.grid()
plt.legend()
plt.xlabel('$I$ / $A$')
plt.ylabel('$U_k$ / $V$')
plt.savefig('Rechteck.pdf')