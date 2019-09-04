import numpy as np 

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

Us5, Is5 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V504_ThermischeElektronenemission/Auswertung/I_s=2.5A.txt', unpack=True)
If5 = 2.5
Uf5 = 6

np.savetxt('1.txt', Is1)
np.savetxt('1.txt', Is2)
np.savetxt('1.txt', Is3)
np.savetxt('1.txt', Is4)
np.savetxt('1.txt', Is5)