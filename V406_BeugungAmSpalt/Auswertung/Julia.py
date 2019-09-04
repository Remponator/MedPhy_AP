import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math


x, y = np.loadtxt('/home/jones/Documents/Praktikum/V406 Beugung am Spalt/Tabelle.txt', unpack=True)
x *= 1e-2
#y *= 1e-6

x_0 = x[np.argmax(y)]
phi = (x - x_0) / (0.928)

plt.clf()
plt.grid()

def theory(phi, A0, b,Z):
    return (A0 * b * np.sinc(b * np.sin(phi) / (633*10**(-9))))**2 + Z

popt, pcov = curve_fit(theory, phi, y, p0=[np.sqrt(np.max(y))/ 1e-4, 1e-5, 18])

print(popt[1])
x = np.linspace(-0.05, 0.05, 1000)
plt.plot(x, theory(x, *popt), 'b-', label='Theoriekurve')
plt.plot(phi, y, 'rx', label='Messwerte')
plt.xlabel(r'$\varphi$ [rad]')
plt.ylabel('I [A] $10^{-6}$')
plt.legend(loc='best')
#plt.savefig('loesung2.pdf')
plt.show()
