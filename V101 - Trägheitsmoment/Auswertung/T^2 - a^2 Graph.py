import numpy as np 
import matplotlib.pyplot as plt 
import scipy.constants as const
import math

x=np.array([0.2635,0.2435,0.2235,0.2035,0.1835,0.1635,0.1435,0.1235,0.1035,0.0835])

T = np.array([6.72,6.16,5.87,5.28,4.72,4.14,3.82,3.60,3.01,3.09])

r = 0.0165

a = np.array([0.28,0.26,0.24,0.22,0.20,0.18,0.16,0.14,0.12,0.10]) - r

fit = np.polyfit(a**2,T**2,1)
fit_fn=np.poly1d(fit)

plt.plot(a**2,T**2,'x', label=r'Messwerte')
plt.plot(a**2,fit_fn(a**2), '-k', label=r'Ausgleichsgerade')
plt.ylabel(r'$T^2 \:/s$')
plt.xlabel(r'$a^2 \:/m $')
plt.legend()
plt.xlim((0.10-r)**2,(0.28-r)**2)
print(fit_fn)
plt.show()