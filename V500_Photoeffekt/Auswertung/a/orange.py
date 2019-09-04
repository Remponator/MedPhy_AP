import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

U_o, I_o = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V500_Photoeffekt/Auswertung/Orange.txt', unpack=True)
U_or =  U_o[3:19]
I_or = I_o[3:19]
#print(U_or)

#Regression Nummer a)

x_regr = np.linspace(0.06,0.6,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,U_or,np.sqrt(I_or))

errors = np.diag(covariance)

m_o = ufloat(params[0],errors[0])
b_o = ufloat(params[1],errors[1])
print('m_o:', m_o)
print('b_o:', b_o)

plt.plot(U_o,np.sqrt(I_o),'y+', label= 'Messwerte')
plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')
axes = plt.gca()
axes.set_ylim([0,0.32])
plt.xlabel(r'$U_{geg}$ / V', size=12)
plt.ylabel(r'$\sqrt{I}$ / nA', size=12)
plt.legend(loc='best')
plt.grid()
plt.savefig('aOrange.png')
#plt.show()
print('U: ',b_o/m_o)
print(I_o)
print(np.sqrt(I_o))