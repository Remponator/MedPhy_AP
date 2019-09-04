import numpy as np 
from uncertainties import ufloat

U, N, I = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V703_Geiger-Mueller-Zaehlrorhr/Auswertung/a).txt', unpack=True)
#U in V, I in mikroA, N in 60s
N_err = np.sqrt(N)

#n = ufloat(N, N_err)
Q = (I*10e-6 * 60) / n
Q_e = Q / 1.602176e-19 #in e0

print('Q: ',Q)
print('Q_e: ',Q_e)