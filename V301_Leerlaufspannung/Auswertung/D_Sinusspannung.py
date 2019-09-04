import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

U = np.array([6,6.5,7.5,8.7,9.1,9.8,9.9,6.2,7.1,7.9])

I = np.array([0.022,0.021,0.0175,0.0105,0.008,0.003,0.0028,0.022,0.019,0.016])

def f(m,I,b):
    return m*I+b

params, covariance = curve_fit(f, I, U)
errors = np.diag(covariance)

print('Ri:', params[0], '+-', errors[0])
print('U0:', params[1], '+-', errors[1])

plt.plot(I, f(I, *params), 'r-', label = r'Ausgleichsgerade')

plt.plot(I, U, 'bx', label=r'Messdaten')

plt.grid()
plt.legend()
plt.xlabel('$I$ / $A$')
plt.ylabel('$U_k$ / $V$')
plt.savefig('Sinusspannung.pdf')