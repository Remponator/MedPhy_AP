import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat

l = np.array([0.67,0.66,0.66,0.66,0.67,0.67,0.66,0.68,0.67])
L1 = np.mean(l) #Länge Draht
dL = np.std(l, ddof=1) / np.sqrt(len(l)) #Fehler des Mittelwerts

L = ufloat(L1,dL)   #Länge Draht

d = np.array([0.00016,0.00017,0.00016,0.00016,0.00017])
D = np.mean(d)  #Durchmesser Draht
dD = np.std(d, ddof=1) / np.sqrt(len(d))
R1 = D/2
dR = dD/2

R = ufloat(R1, dR)  #Radius Draht

t = np.array([18.544,18.540,18.551,18.570,18.252,18.537,18.579,18.563,18.554,18.589])
T1 = np.mean(t) 
dT = np.std(t, ddof=1) / np.sqrt(len(t))

T = ufloat(T1, dT)      #Periodendauer

Mk = ufloat(0.5883, 0.0004*0.5883) #Masse Kugel

Rk = ufloat(0.025515, 0.0004*0.025515)   #Radius Kugel

tetaKugel = (2/5)*Mk*(Rk**2)
tetaHalt = 22.5*10**(-7)

teta = tetaKugel + tetaHalt #Trägheitsmoment gesamt

#Berechnung von G

def G(teta, L, T, R):
    return (8*math.pi*teta*L/((T**2)*(R**4)))

print('G(teta, L, T, R):',"{:.5f}".format(G(teta, L, T, R)))    #Nachkommastellen printen
