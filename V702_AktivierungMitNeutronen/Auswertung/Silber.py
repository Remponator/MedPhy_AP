import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

N_0 = 244
t_0 = 900 #sec
N0 = np.log((N_0/t_0)*9)
dN0 = np.sqrt(N0)

N = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V702_Aktivierung-mit-Neutronen/Auswertung/Silber.txt', unpack=True)

Nplot = N[0:12]
nplot = np.linspace(0,12,12)
tplot = 9*nplot #sec
n = np.linspace(0,50,50)
t = 9*n #sec
plt.plot(tplot,np.log(Nplot),'b.')
'''plt.ylabel('N')
plt.xlabel('t [s]')
plt.legend(loc='best')
plt.grid()'''
#plt.show()
N = np.log(N)-N0

N_err = np.sqrt(N)-dN0

#langlebige

#plt.errorbar(t, N, xerr=0.2, yerr=N_err,fmt='b.', label = r'Messwerte')
#plt.plot(t,N, 'b.', label = r'Messwerte')
x_regr = np.linspace(1,460,1000)

def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit,t,N)

errors = np.diag(covariance)

m = ufloat(params[0],errors[0])
b = ufloat(params[1],errors[1])
print('m1:', m)
print('b1: ',b)

'''plt.plot(x_regr, lin_fit(x_regr, *params), 'r-', label = r'Ausgleichsfunktion')

plt.ylabel('$\log$(N)')
plt.xlabel('t [s]')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([0,460])
axes.set_ylim([0,4.2])
plt.grid()'''

#plt.show()

N0_1 = unp.exp(b)
T1 = np.log(0.5)/m

print('T1: ',T1)
print('N0_1: ',N0_1)

#########
N = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V702_Aktivierung-mit-Neutronen/Auswertung/Silber.txt', unpack=True)

N3 = N[13:50]  #sehr früh da sonst negativ

n = np.linspace(13,50,37)
t = 9*n #sec
#N3 = N3-N0_1*np.exp(0.005*t)

N3 = np.log(N3)-N0
N_err = np.sqrt(N3)-dN0

#plt.errorbar(t, N3, xerr=0.2, yerr=N_err,capsize=2,fmt='b+', label = r'Messwerte mit Fehlerbalken')
plt.plot(t,N3,'b.',label = r'Messwerte')
x_regr = np.linspace(30,470,1000)

def lin_fit3(x3,m3,b3):
    return m3*x3+b3

params, covariance = curve_fit(lin_fit3,t,N3)

errors = np.diag(covariance)

m3 = ufloat(params[0],errors[0])
b3 = ufloat(params[1],errors[1])
#print('m:', m2)
#print('b: ',b2)

plt.plot(x_regr, lin_fit3(x_regr, *params), 'r-', label = r'Regression des langsamen Zerfalls')

plt.ylabel('$\log$(N)')
plt.xlabel('t [s]')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([100,460])
plt.grid()

plt.show()

N0_1 = unp.exp(b3)
T3 = np.log(0.5)/m3

#print('T3: ',T3)
#print('N0_3: ',N0_3)

#kurzlebige bis 63s
N2 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V702_Aktivierung-mit-Neutronen/Auswertung/Silber.txt', unpack=True)

N2 = N2[13]  #sehr früh da sonst negativ
#N0_1 = unp.nominal_values(N0_1)
#n = np.linspace(1,13,13)
#t = 9*n #sec
print('N2:',N2-N0_1*np.exp(0.005*117))
print('N1:',N0_1*np.exp(0.005*117))
'''N2 = N2-N0_1*np.exp(0.005*t)
print(N2)
print(np.sqrt(N2))
N2 = np.log(N2)-N0
N_err = np.sqrt(N2)-dN0

#plt.errorbar(t, N2, xerr=0.2, yerr=N_err,fmt='bx', label = r'Messwerte des schnellen Zerfalls mit Fehlerbalken')
plt.plot(t,N2,'bx',label = r'Messwerte des schnellen Zerfalls')

x_regr = np.linspace(1,120,1000)

def lin_fit2(x2,m2,b2):
    return m2*x2+b2

params, covariance = curve_fit(lin_fit2,t,N2)

errors = np.diag(covariance)

m2 = ufloat(params[0],errors[0])
b2 = ufloat(params[1],errors[1])
print('m:', m2)
print('b: ',b2)

plt.plot(x_regr, lin_fit2(x_regr, *params), 'k-', label = r'Regression des schnellen Zerfalls')

plt.ylabel('$\log$(N)')
plt.xlabel('t [s]')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([0,110])
axes.set_ylim([-0.1,4.1])
plt.grid()

plt.ylabel('$\log$(N)')
plt.xlabel('t [s]')
plt.legend(loc='best')
axes = plt.gca()
axes.set_xlim([0,460])
axes.set_ylim([0,4.1])
plt.show()

N0_2 = unp.exp(b2)
T2 = np.log(0.5)/m2

print('T2: ',T2)
print('N0_2: ',N0_2)
'''

