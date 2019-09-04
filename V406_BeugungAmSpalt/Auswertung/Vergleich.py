import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dx1,dI1 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V406_Beugung_am_Spalt/Auswertung/T3.txt', unpack=True)

x1 = dx1 * 10**(-3)
I1 = dI1 * 10**(-9)
l1 = 990  * 10**(-3) #Abstand vom optischen Element in mm
Id1 = 4.5  * 10**(-9)#Dunkelstrom in A*10^-9
b1 = 0.4* 10**(-3) #Spaltbreite in mm
j1 = 633*10**(-9) #Laser Wellenlänge 
Ao1 = 110 * 10**(-9) #Amplitude bei 0 in A*10^-9

Im1 = I1 - Id1 #gemessener Strom ohne Dunkelstrom

phi1 = x1/l1

#xdata = np.linspace(-0.005,0.005,59)
#phid = xdata/l

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

plt.plot(phi1,Im1,'r-')
plt.plot(phi,I,'b-')
plt.show()