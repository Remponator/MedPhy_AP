import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

U = np.array([0.15, 0.48, 0.7, 0.85, 0.95, 1.1, 1.2, 1.25, 1.3, 1.31, 1.4])
U1 = unp.uarray(U, 0.02*U)

I1 = np.array([88,69,56,47,40,36,32,29,27,24,23])
I = 0.001*I1

def f(I, m, b):     
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
#plt.savefig('B_Innenwiderstand.pdf')
plt.show()