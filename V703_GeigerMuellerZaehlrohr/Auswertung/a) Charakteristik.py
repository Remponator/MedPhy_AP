import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
U_r, Nn, In = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V703_Geiger-Mueller-Zaehlrorhr/Auswertung/Regr.txt', unpack=True)
U, n, I = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V703_Geiger-Mueller-Zaehlrorhr/Auswertung/a).txt', unpack=True)
#U in V, I in mikroA, N in 60s

N = n/60 #Anzahl Teilchen pro sekunde

'''N_err = np.sqrt(N)

#Plot Charakteristik
plt.errorbar(U, N+N_err, xerr=0.4, yerr=N_err,capsize=2,fmt='x', label = r'Messwerte')
plt.ylabel('N [1/s]')
plt.xlabel('U [V]')
plt.legend(loc='best')
plt.grid()
plt.show()
#plt.savefig('Charakteristik.pdf')
#print(N_err)
print(N)'''
#Regression
N_r = Nn/60
Nr_err = np.sqrt(N_r/60)

plt.errorbar(U_r, N_r, xerr=0.2, yerr=Nr_err,capsize=2,fmt='x', label = r'Messwerte')

x_regr = np.linspace(400,600,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,U_r,N_r)

errors = np.diag(covariance)

m = ufloat(params[0],errors[0])
b = ufloat(params[1],errors[1])
print('m:', m)
print('b:', b)

plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')

plt.ylabel('N [1/s]')
plt.xlabel('U [V]')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([400,600])
plt.grid()
plt.show()
#plt.savefig('Charakteristik_Regression.pdf')