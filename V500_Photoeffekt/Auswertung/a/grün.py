import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

U_gr, I_gr = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V500_Photoeffekt/Auswertung/grün.txt', unpack=True)

#Regression

x_regr = np.linspace(0,0.62,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,U_gr,np.sqrt(I_gr))

errors = np.diag(covariance)

m = ufloat(params[0],errors[0])
b = ufloat(params[1],errors[1])
print('m:', m)
print('b:', b)

plt.plot(U_gr,np.sqrt(I_gr),'g+', label=r'Messwerte')
plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')
axes = plt.gca()
axes.set_ylim([0,0.51])
plt.xlabel(r'$U_{geg}$ / V', size=12)
plt.ylabel(r'$\sqrt{I}$ / nA', size=12)
plt.legend(loc='best')
plt.grid()
plt.savefig('aGrün.png')
print('U: ',b/m)
print(np.sqrt(I_gr))