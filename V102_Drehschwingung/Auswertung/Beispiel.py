import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

y=np.array([0.003411, 0.003277, 0.003235, 0.003183, 0.003133, 0.003076, 0.003038, 0.002993, 0.002949, 0.002949])
x=np.array([-9.0996, -9.197, -9.270, -9.359, -9.430, -9.442, -9.482, -9.525, -9.556, -9.580])


def f(x, m, b):         #ausgeichsgrade
    return m*x+b

params, covariance = curve_fit(f, x, y)
errors = np.diag(covariance)

print('m:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])

plt.plot(x, f(x, *params), 'r-', label = r'Ausgleichsgerade')       #ausgleichsgrade


plt.plot(x, y, 'bo', label=r'Messdaten')
plt.xlabel(r'${ln(\eta*Pa^{-1}s^{-1})}$')
plt.xlim(-9.000,-9.700)

plt.ylabel(r'$1/T/K^{-1}$')
plt.ylim(0.002800, 0.003500)

plt.grid()

plt.legend(loc='best')

plt.tight_layout()

plt.show()


plt.savefig('GraphViskosität.pdf')
