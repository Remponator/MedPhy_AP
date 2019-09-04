import numpy as np 
from uncertainties import ufloat

#Bestimmung der Totzeit per 2-Quellen-Methode

U = 450 #in V
N_1 = ufloat(14034,118)
N_2 = ufloat(13155,115)
N_12 = ufloat(26491,163)

T = (N_1 + N_2 - N_12)/(2*N_1*N_2) * 10e6 #Totzeit in mikroSekunden
print(T)