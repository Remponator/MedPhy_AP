import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

U_zy, I_zy = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V500_Photoeffekt/Auswertung/zyan.txt', unpack=True)

U_zyr =  U_zy[0:7]
I_zyr = I_zy[0:7]

#Regression

x_regr = np.linspace(0.3,1.2,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,U_zyr,np.sqrt(I_zyr))

errors = np.diag(covariance)

m = ufloat(params[0],errors[0])
b = ufloat(params[1],errors[1])
print('m:', m)
print('b:', b)

plt.plot(U_zy,np.sqrt(I_zy),'c+', label = r'Messwerte')
plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')
axes = plt.gca()
axes.set_ylim([0,0.61])
plt.xlabel(r'$U_{geg}$ / V', size=12)
plt.ylabel(r'$\sqrt{I}$ / nA', size=12)
plt.legend(loc='best')
plt.grid()
plt.savefig('aZyan.png')
print('U: ',b/m)
print(np.sqrt(I_zy))