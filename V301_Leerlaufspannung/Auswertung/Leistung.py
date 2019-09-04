import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Expeiment

U = np.array([0.15, 0.48, 0.7, 0.85, 0.95, 1.1, 1.2, 1.25, 1.3, 1.31, 1.4])
U1 = unp.uarray(U, 0.02*U)

I1 = np.array([88,69,56,47,40,36,32,29,27,24,23])
I = 0.001*I1

Ra = U/I
N_ex = Ra*I**2

plt.plot(Ra, N_ex, 'rx')
print(Ra)
print(N_ex)
#Theorie

U0 = 1.6
RI = 19
x = np.linspace(1, 61, 1000)

def f (U0,x,RI):
    return U0**2 * x /(RI+x)**2

plt.plot(x, f(U0,x,RI), 'b-')

plt.xlabel('Belastungswiderstand $R_{a}$ [Ω]')
plt.ylabel('Leistung $P$ [W]')
plt.legend(loc='best')
plt.show()