import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp

Mb = 234.82 #Masse Becher in Gramm
Mk = np.array([578.93,530.96,502.22])-Mb #Gewicht Wasser kalt (mx)
Mm = np.array([816.67,710.59,701.10])-Mb #Gewicht Wasser gemischt
Mh = Mm - Mk #Gewicht Wasser heiß (my)
cw = 4.18 #Wärmekapazität Wasser bei ca. 40 Grad Celsius

Tk = np.array([22.6,25.4,25.3])+237.5 #Temperatur kaltes Wasser in K (Tx)
Th = np.array([100,100,100])+237.5 #Temperatur heißes Wasser in K (Ty)
Tm = np.array([49.2,50.4,54.7])+237.5 #Temperatur gemischt 

#Wärmekapazität Kalorimeter
cgmg = np.array((cw*Mh*(Th-Tm)-4.18*Mk*(Tm-Tk))/(Tm-Tk))

mcgmg = np.mean(cgmg)

dcgmg = np.std(cgmg, ddof=1) / np.sqrt(len(cgmg))

CgMg = ufloat(mcgmg,dcgmg)

print('cgmg:',CgMg)

#Wärmekapazität Alu

Tw1 = np.array([24.6,22.6,22.1])+237.5 #Temperatur Wasser
Tp1 = 100+273.5 #Temperatur Probe
Tm1 = np.array([27.7,26.1,25.9])+273.5 #Temperatur Mischung

Mw1 = np.array([894.00,873.21,851.86])-Mb #Gewicht Wasser - Becher
Mp1 = 155 #Masse Probe Alu

ck1 = ((cw*Mw1+CgMg)*(Tm1-Tw1))/(Mp1*(Tp1-Tw1))

mck1 = np.mean(ck1)


print('ck Alu: ',mck1)

#Wärmekapazität Blei

Tw2 = np.array([22.9,22.6,22.0])+237.5 #Temperatur Wasser
Tp2 = 100+273.5 #Temperatur Probe
Tm2 = np.array([25.0,24.6,24.4])+273.5 #Temperatur Mischung

Mw2 = (np.array([850.53,863.35,862.09])-Mb) #Gewicht Wasser - Becher
Mp2 = 542.68 #Masse Probe Blei

ck2 = ((cw*Mw2+CgMg)*(Tm2-Tw2))/(Mp2*(Tp2-Tw2))

mck2 = np.mean(ck2)

print('ck Blei: ',mck2)

#MolWärme Alu

cv1 = ck1*27-(9*(23.5*(10**-6)**2)*(75*(10**9))*(27/(2.7*10**6))*Tm1)

mcv1 = np.mean(cv1)

print('Cv Alu:',mcv1)
print(cv1)

#Molwärme Blei

cv2 = ck2*207.2-(9*(29.0*(10**-6)**2)*(42*(10**9))*(207.2/(11.35*10**6))*Tm2)

mcv2 = np.mean(cv2)

print('Cv Blei:',mcv2)
print(cv2)

R = 8.314
print('3R = ',3*R)