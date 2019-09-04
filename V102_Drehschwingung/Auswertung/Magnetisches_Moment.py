import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 


l = np.array([0.67,0.66,0.66,0.66,0.67,0.67,0.66,0.68,0.67])
L1 = np.mean(l) #Länge Draht ohne Fehler
dL = np.std(l, ddof=1) / np.sqrt(len(l)) #Fehler des Mittelwerts

L = ufloat(L1,dL)  #Länge Draht

d = np.array([0.00016,0.00017,0.00016,0.00016,0.00017])
Du = np.mean(d)  #Durchmesser Draht
dD = np.std(d, ddof=1) / np.sqrt(len(d))
R1 = Du/2
dR = dD/2

R = ufloat(R1, dR)  #Radius Draht

t = np.array([18.544,18.540,18.551,18.570,18.252,18.537,18.579,18.563,18.554,18.589])
Tges = np.mean(t) 
dT = np.std(t, ddof=1) / np.sqrt(len(t))

T = ufloat(Tges, dT)      #Periodendauer

Mk = ufloat(0.5883, 0.0004*0.5883) #Masse Kugel

Rk = ufloat(0.025515, 0.0004*0.025515)   #Radius Kugel

tetaKugel = (2/5)*Mk*(Rk**2)
tetaHalt = 22.5*10**(-7)

teta = tetaKugel + tetaHalt #Trägheitsmoment gesamt

#Berechnung der Mittelwerte
t0 = np.array([11.310,11.102,11.101])               #Array der Werte
T00 = np.mean(t0)                                   #Mittelwert
dT0 = np.std(t0, ddof=1) / np.sqrt(len(t0))         #Fehler des Mittelwerts
T0 = ufloat(T00,dT0)                                #Periodendauer mit Fehler

t1 = np.array([8.756,8.779,8.762])
T01 = np.mean(t1)
dT1 = np.std(t1, ddof=1) / np.sqrt(len(t1))
T1 = ufloat(T01,dT1)

t2 = np.array([7.467,7.465,7.460])
T02 = np.mean(t2)
dT2 = np.std(t2, ddof=1) / np.sqrt(len(t2))
T2 = ufloat(T02,dT2)

t3 = np.array([6.583,6.608,6.596])
T03 = np.mean(t3)
dT3 = np.std(t3, ddof=1) / np.sqrt(len(t3))
T3 = ufloat(T03,dT3)

t4 = np.array([5.975,5.973,5.981])
T04 = np.mean(t4)
dT4 = np.std(t4, ddof=1) / np.sqrt(len(t4))
T4 = ufloat(T04,dT4)

t5 = np.array([5.521,5.526,5.519])
T05 = np.mean(t5)
dT5 = np.std(t5, ddof=1) / np.sqrt(len(t5))
T5 = ufloat(T05,dT5)

t6 = np.array([5.136,5.132,5.142])
T06 = np.mean(t6)
dT6 = np.std(t6, ddof=1) / np.sqrt(len(t6))
T6 = ufloat(T06,dT6)

t7 = np.array([4.578,4.577,4.865])
T07 = np.mean(t7)
dT7 = np.std(t7, ddof=1) / np.sqrt(len(t7))
T7 = ufloat(T07,dT7)

t8 = np.array([4.558,4.587,4.556])
T08 = np.mean(t8)
dT8 = np.std(t8, ddof=1) / np.sqrt(len(t8))
T8 = ufloat(T08,dT8)

t9 = np.array([4.336,4.330,4.344])
T09 = np.mean(t9)
dT9 = np.std(t9, ddof=1) / np.sqrt(len(t9))
T9 = ufloat(T09,dT9)


Tges = np.array([T0,T1,T2,T3,T4,T5,T6,T7,T8,T9]) #Schwingungsdauer

I1 = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])    #Stromstärke
dI = np.array([0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25])      #Fehler Stromstärke (5%)

I = unp.uarray(I1, dI)

mu = const.physical_constants["mag. constant"] #Magnetische Feldkonstante
Mu = mu[0]  #Wert von der Konstante
X = ufloat(0.072,0)   #Radius und Abstand Helmholtzspule
N = ufloat(80,0)  #Windungen der Spulen

def B(X,N,Mu,I):                    
    return I*Mu*N*X**2/((2*X**2)**(3/2))    #Magnetfeld B

Bm = np.mean(B(X,N,Mu,I))

def G(teta, L, T, R):
    return (8*math.pi*teta*L/((T**2)*(R**4)))   #Trägheitsmodul G

D = math.pi*G(teta, L, T, R)*R**4/(2*L)    #Richtgröße des Zylinders

x = (unp.nominal_values(B(X,N,Mu,I)))
y = (unp.nominal_values(1/Tges**2))

def f(x, m, b):         #ausgeichsgrade
    return m*x+b

params, covariance = curve_fit(f, x, y)
errors = np.diag(covariance)

print('m:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])

plt.plot(x, f(x, *params), 'r-', label = r'Ausgleichsgerade')       #ausgleichsgrade

ST = ufloat(20.617223278946874, 0.16288964210396956)     #Steigung der Ausgleichsgeraden

plt.plot(x, y, 'bo', label=r'Messdaten')
#plt.show()

def magnet(ST,Bm,D,teta):
    return 4*(math.pi)**2*ST*teta-(D/Bm)

print('magnet(ST,Bm,D,teta):',"{:.5f}".format(magnet(ST,Bm,D,teta)))