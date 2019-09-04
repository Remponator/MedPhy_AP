
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dx,dI = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V406_Beugung_am_Spalt/Auswertung/T2.txt', unpack=True)

x = dx * 10**(-3)
I = dI * 10**(-9)
l = 990  * 10**(-3) #Abstand vom optischen Element in mm
Id = 4.5  * 10**(-9)#Dunkelstrom in A*10^-9
b = 0.4* 10**(-3) #Spaltbreite in mm
j = 633*10**(-9) #Laser Wellenlänge 
Ao = 110 * 10**(-9) #Amplitude bei 0 in A*10^-9

Im = I - Id #gemessener Strom ohne Dunkelstrom

phi = x/l

#xdata = np.linspace(-0.005,0.005,59)
#phid = xdata/l

plt.plot(phi,Im,'rx')

def f (phi,b,A,B,C,D,Z):
    return A*b**2*(j/(np.pi*b*np.sin(C*phi)))**2*(np.sin(D*np.pi*b*np.sin(B*phi)/j))**2 + Z

params, covariance = curve_fit(f, phi, Im, bounds=([10**(-5),-0.005,0.16,-0.005,-0.005,0],[5*10**(-3),0.655,0.3,1,1,0.000000025]))

errors = np.diag(covariance)

print('b:', params[1], '+-', errors[1])
print('A:', params[0], '+-', errors[0])
#print('B:', params[2], '+-', errors[2])
#print('C:', params[3], '+-', errors[3])
#print('D:', params[4], '+-', errors[4])

plt.plot(np.linspace(-0.005,0.005,1000), f(np.linspace(-0.005,0.005,1000), *params), 'b-', label = r'Ausgleichsfunktion') 

plt.grid()
plt.xlabel(r'$\varphi \,\, / \,\, \mathrm{rad}$')
plt.ylabel(r'$I \,\, / \,\, \mu\mathrm{A}$')
plt.show()