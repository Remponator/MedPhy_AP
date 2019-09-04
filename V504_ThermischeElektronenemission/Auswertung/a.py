import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Us: Anodenspannung in V, Is Anodenstrom in mA
Us1, Is1 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/I_s=2A.txt', unpack=True)
If1 = 2 #Heizstrom in A
Uf1 = 4 #Heizspannung in V

Us2, Is2 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/I_s=2.1A.txt', unpack=True)
If2 = 2.1
Uf2 = 4.5

Us3, Is3 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/I_s=2.2A.txt', unpack=True)
If3 = 2.2
Uf3 = 4.8

Us4, Is4 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/I_s=2.3A.txt', unpack=True)
If4 = 2.3
Uf4 = 5

#maximaler Heizstrom
Us5, Is5 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/I_s=2.5A.txt', unpack=True)
If5 = 2.5
Uf5 = 6

#Kennlinien
'''plt.plot(Us1,Is1,'r+', label='$I_f = 2.0 A$')
plt.plot(Us2,Is2,'b+', label='$I_f = 2.1 A$')
plt.plot(Us3,Is3,'g+', label='$I_f = 2.2 A$')
plt.plot(Us4,Is4,'y+', label='$I_f = 2.3 A$')
plt.plot(Us5,Is5,'m+', label='$I_f = 2.5 A$')
plt.ylabel('I / mA')
plt.xlabel('U / V')
axes = plt.gca()
axes.set_xlim([0,250])
axes.set_ylim([0,3.1])
plt.legend(loc='best')
plt.grid()
plt.savefig('Kennlinien.pdf')'''

#Raumladungsgesetz - Langmuir-Schottky
def lin_fit(x,m,b):
    return m*x+b

params, covariance = curve_fit(lin_fit, np.log(Us5), np.log(Is5))
errors = np.diag(covariance)

print('q:', params[0],'+-',errors[0]) #q (Exponent)
print('b:', params[1],'+-',errors[1]) #ln(K/AV^-1)

'''plt.plot(np.log(Us5),np.log(Is5),'k+', label='Messwerte')
plt.plot(np.log(Us5), lin_fit(np.log(Us5), *params), 'b-', label = r'Ausgleichsfunktion')
plt.ylabel(r'$ln\left(\frac{I}{A}\right)$', size =13)
plt.xlabel(r'$ln\left(\frac{U}{V}\right)$', size =13)
plt.legend(loc='best')
plt.tight_layout()
axes = plt.gca()
axes.set_xlim([1.6,5.6])
axes.set_ylim([-4.44,1.2])
plt.grid()
plt.savefig('b.pdf')'''
