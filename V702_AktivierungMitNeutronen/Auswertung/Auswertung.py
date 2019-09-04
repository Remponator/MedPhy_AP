import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

N_0 = 244
t_0 = 900 #sec
N0 = np.log((N_0/t_0)*225)
dN0 = np.sqrt(N0)

N = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V702_Aktivierung-mit-Neutronen/Auswertung/Indium.txt', unpack=True)

N = np.log(N)

n = np.linspace(1,20,20)
t = 225*n #sec

N_err = np.sqrt(N)-dN0

plt.errorbar(t, N, xerr=0.2, yerr=N_err,capsize=2,fmt='bx', label = r'Messwerte')

x_regr = np.linspace(0,4700,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,t,N)

errors = np.diag(covariance)

m = ufloat(params[0],errors[0])
b = ufloat(params[1],errors[1])
print('m:', m)

plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')

plt.ylabel('$\log$(N)')
plt.xlabel('t [s]')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([0,4700])
plt.grid()

plt.show()

T = unp.log(2)/(-m)
k = unp.exp(b)

print(T)
print(k)