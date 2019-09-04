import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dx,I = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V406_Beugung_am_Spalt/Auswertung/T2.txt', unpack=True)

x = dx*10**(-3)
l = 990*10**(-3)  #Abstand vom optischen Element in mm
Id = 4.5 #Dunkelstrom in A*10^-9
b = 0.4*10**(-3) #Spaltbreite in mm
j = 633*10**(-9) #Laser Wellenlänge in mm
Ao = 110 #Amplitude bei 0 in A*10^-9

Im = I - Id #gemessener Strom ohne Dunkelstrom
phi = x/l

#def f (Ao,b,j,phi):
#    return (Ao**2)*(b**2)*(((j)/(np.pi*b*np.sin(phi)))**2)*(np.sin((np.pi*b*np.sin(phi))/j))**2

#plt.plot(phi,Im,'r+')

#params, covariance = curve_fit(f, phi, Im)

#print('b:', params[0])

#plt.plot(phi, f(phi, *params), 'b-', label = r'Ausgleichsfunktion') 
#plt.grid()
#plt.show()
print(I)
print(Im)