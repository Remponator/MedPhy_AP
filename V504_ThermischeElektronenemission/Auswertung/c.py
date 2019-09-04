import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

Us, Is = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/c.txt', unpack=True)

Is_c = Is*1e-9 #Is in SI
R = 1e6 #1MOhm -> Innenwiderstand Amperemeter

Uc = Us+Is_c*R #Korrektur nach Widerstand

#Messwertr nach Korrektur 
plt.plot(Uc,Is,'r+',label='Messwerte')
plt.xlabel(r'$U_c$ / V')
plt.ylabel('I / nA')
plt.legend(loc='best')
plt.grid()
plt.savefig('c_Messwerte.pdf')

#Regression
def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,Uc,np.log(Is))

errors = np.diag(covariance)

m_c = ufloat(params[0],errors[0])
b_c = ufloat(params[1],errors[1])
print('m_c:', m_c)
print('b_c:', b_c)

'''plt.plot(Uc,np.log(Is),'k+', label='Messwerte')
plt.plot(Uc, lin_fit(Uc, *params), 'b-', label = r'Ausgleichsfunktion')
plt.ylabel(r'$ln\left(\frac{I}{nA}\right)$', size=13)
plt.xlabel(r'$U_c$ / V')
plt.legend(loc='best')
plt.tight_layout()
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([-2.3,2.7])
plt.grid()
plt.savefig('c_Regression.pdf')'''

k_b = 1.3806488e-23 #Boltzmankonst.
e_0 = 1.602e-19 #Coulomb

T = e_0/(k_b*m_c)
print(T)

