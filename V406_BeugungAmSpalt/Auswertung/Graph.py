
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dx,dI = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V406_Beugung_am_Spalt/Auswertung/Einzelspalt1.txt', unpack=True)

x = dx * 10**(-3)
I = dI * 10**(-9)
l = 990  * 10**(-3) #Abstand vom optischen Element in mm
Id = 4.5  * 10**(-9)#Dunkelstrom in A*10^-9
b = 0.1* 10**(-3) #Spaltbreite in mm
j = 633*10**(-9) #Laser Wellenlänge 
Ao = 23 * 10**(-9) #Amplitude bei 0 in A*10^-9

#Im = I - Id #gemessener Strom ohne Dunkelstrom

phi = x/l

#xdata = np.linspace(-0.005,0.005,59)
#phid = xdata/l

plt.plot(phi,I,'rx')

def f (phi,b,A,B,C,D):
    return A*b**2*(j/(np.pi*b*np.sin(C*phi)))**2*(np.sin(D*np.pi*b*np.sin(B*phi)/j))**2

params, covariance = curve_fit(f, phi, I, bounds=([10**(-10),-0.02,0.016,-0.02,-0.05],[5*10**(-3),0.355,0.3,0.8,0.8]))

errors = np.diag(covariance)

print('b:', params[0], '+-', errors[0])
#print('A:', params[1], '+-', errors[1])
#print('B:', params[2], '+-', errors[2])
#print('C:', params[3], '+-', errors[3])
#print('D:', params[4], '+-', errors[4])

plt.plot(phi, f(phi, *params), 'b-', label = r'Ausgleichsfunktion') 

plt.grid()
plt.show()

'''
phi1 = np.linspace(-0.005,0.005,1000000)
F = Ao**2*b**2*(j/(np.pi*b*np.sin(phi1)))**2*(np.sin(np.pi*b*np.sin(phi1)/j))**2
plt.plot(phi1,F,'r-')'''
