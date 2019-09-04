import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

U_o, I_o = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V500_Photoeffekt/Auswertung/Orange.txt', unpack=True)

plt.plot(U_o,I_o**2,'y+')
plt.show()

