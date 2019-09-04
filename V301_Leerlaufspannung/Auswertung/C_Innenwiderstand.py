import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

U = np.array([4, 3.5, 3.2, 3, 2.9, 2.8, 2.7, 2.6, 2.6, 2.45, 2.4])

I = np.array([0.12,0.09,0.074,0.063,0.057,0.054,0.05,0.045,0.043,0.035,0.031])

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
plt.savefig('C_Innenwiderstand.pdf')