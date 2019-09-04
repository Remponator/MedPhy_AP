import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

Ug = np.array([0.52,0.61,1.10,1.25,1.67]) #Grenzspannung von: gelb, grün, zyan, blau, uv in V
l = np.array([578,546,492,434,365]) #Wellenlänge in nm
f = 299792458/(l*10**-9) #frequenz

x_regr = np.linspace(5e14,8.5e14,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,f,Ug)

#Verhältnis h/e0 & Austrittsarbeit Ak
errors = np.diag(covariance)

m_o = ufloat(params[0],errors[0])
b_o = ufloat(params[1],errors[1])
print('h/e0:', m_o)
print('Ak:', b_o)

plt.plot(f,Ug,'bx', label=r'Messwerte')
plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')
plt.xlabel(r'Frequenz / Hz')
plt.ylabel(r'U / V')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([5e14,8.5e14])
plt.grid()
#plt.savefig('bPlot.png')
#plt.show()
