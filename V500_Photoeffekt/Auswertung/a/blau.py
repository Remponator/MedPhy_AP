import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

U_bl, I_bl = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V500_Photoeffekt/Auswertung/blau.txt', unpack=True)

#U_blr =  U_bl[3:19]
#I_blr = I_bl[3:19]
#Regression

x_regr = np.linspace(0,1.3,1000) 
def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,U_bl,np.sqrt(I_bl))

errors = np.diag(covariance)

m = ufloat(params[0],errors[0])
b = ufloat(params[1],errors[1])
print('m:', m)
print('b:', b)

plt.plot(U_bl,np.sqrt(I_bl),'b+', label=r'Messwerte')
plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')
axes = plt.gca()
axes.set_ylim([0,0.5])
plt.xlabel(r'$U_{geg}$ / V', size=12)
plt.ylabel(r'$\sqrt{I}$ / nA', size=12)
plt.legend(loc='best')
plt.grid()
plt.savefig('aBlau.png')
print('U: ',b/m)
print(np.sqrt(I_bl))