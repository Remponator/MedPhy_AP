from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

t_1 = np.loadtxt("/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V207-DasKugelfall-ViskosimeterNachHoeppler-/Auswertung/t1.txt", unpack=True)

t_2 = np.loadtxt("/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/V207-DasKugelfall-ViskosimeterNachHoeppler-/Auswertung/t2.txt", unpack=True)

r_1 = 0.0155/2 #m
r_2 = 0.0158/2
m_1 = 0.00484 #kg
m_2 = 0.00536
K_kl = 7.640*(10**-8) #Pam^3/kg
mu_W = 0.001 #Pas
rho_Fl = 998.2 #kg/m^3

mt_1 = np.mean(t_1)
dt_1 = np.std(t_1, ddof=1) / np.sqrt(len(t_1))

t1 = ufloat(mt_1,dt_1)

mt_2 = np.mean(t_2)
dt_2 = np.std(t_2, ddof=1) / np.sqrt(len(t_2))

t2 = ufloat(mt_2,dt_2)

def rho_1(r_1,m_1):
    return (3*m_1)/(4*math.pi*(r_1**3))

def rho_2(r_2,m_2):
    return (3*m_2)/(4*math.pi*(r_2**3))

v_1 = 0.1/t1
v_2 = 0.1/t2

def mu_1(K_kl,rho_1,t1,rho_Fl):
    return K_kl*(rho_1(r_1,m_1)-rho_Fl)*t1

def Re1(rho_1,r_1,mu_W):
    return (rho_1(r_1,m_1)*v_1*(r_1*2))/mu_W
def Re2(rho_2,r_2,mu_W):
    return (rho_2(r_2,m_2)*v_2*(r_2*2))/mu_W

def K_gr(mu_W,rho_Fl,rho_2,t2):
    return (mu_W)/((rho_2(r_2,m_2)-rho_Fl)*t2)

print("t_kl =",t1)
print("t_gr =",t2)
print("K_kl =",K_kl)
print("K_gr =",K_gr(mu_W,rho_Fl,rho_2,t2))
print("Mu =",mu_1(K_kl,rho_1,t1,rho_Fl))
print("rho_kl =",rho_1(r_1,m_1))
print("rho_gr =",rho_2(r_2,m_2))
print("Re1 =",Re1(rho_1,r_1,mu_W))
print("Re2 =",Re2(rho_2,r_2,mu_W))
