# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:43:58 2016

@author: fiepsi
"""

import numpy as np
import matplotlib.pyplot as plt
#from uncertainties import unumpy as unp
#from uncertainties import correlated_values
from scipy.optimize import curve_fit
import matplotlib as mpl
rc = mpl.rc

#%%set up matplotlib
fontsize        = 14
legendfontsize  = fontsize
textwidth       = (210 - 2*30)/25.4
figwidth        = textwidth - 0.1
figheight       = figwidth/2

font = {'family' : 'serif',
        'weight' : 'normal',
        'serif'  : ['Computer Modern Roman'],
        'size'   : fontsize}
rc('font', **font)  # pass in the font dict as kwargs
# if we wanna use tex in the strings
rc('text', usetex=True)
# add the ams packages to the latex preamble for e.g. \mathfrak
rc('text.latex', preamble = ','.join('''
\\usepackage{amsmath}
\\usepackage{amssymb}'''.split()))

#rc('text.latex', preamble = ','.join('''
#\usepackage{amsmath}
#\usepackage{amssymb}
#'''.split()))

# set default figsize
rc('figure' , figsize=(figwidth,figheight))

# create new plot and erase, if old version is present
try:
    plt.close(fig)
except NameError:
    pass
#%%

#L     = 1.142 # in m L_1
wl    = 633*1e-9 # m Wellenlänge lambda
L     = 0.835 #L_2
Ld     = 0.957#L_D

dstr  = 6*1e-11 #Dunkelstrom in Ampere

#%% Einzelspalt 1

#I1, Pos1 = np.loadtxt('einzel1.txt', skiprows=1, unpack=True)

#I1       = I1*1e-6 - dstr # umrechnen in Ampere
#zeta     = Pos1*1e-3
#zeta_0   = zeta[np.argmax(I1)]
#phi      = (zeta - zeta_0)/L

#def theory(phi, A0, b):
#    return (A0 * b * np.sinc(b * np.sin(phi) / wl))**2

#popt1, pcov1 = curve_fit(theory, phi, I1, p0 = [np.sqrt(np.max(I1)) / 1e-4, 1e-4])

#print(popt1, np.sqrt(np.diag(pcov1)), sep='n')
#print(popt1[1])

#es1_fig      = plt.figure(figsize = [10.0, 2.0])
#es1_fig      = es1_fig.add_subplot(111)
#linien_dicke = 1.5

#x = np.linspace(-0.004, 0.004, 100)
#plt.plot(x, theory(x, popt1[0], popt1[1])*1e6, 'k-', label='Ausgleichsrechnung')
#plt.plot(phi, I1*1e6, 'g.', label='Messdaten')
#plt.xlabel(r'$\varphi \,\, / \,\, \mathrm{rad}$')
#plt.ylabel(r'$I \,\, / \,\, \mu\mathrm{A}$')
#plt.legend(loc='best')
#plt.savefig('einzel1.pdf', bbox_inches='tight')

#plt.figure(figsize=[figwidth,figwidth])
#plt.plot(zeta, I1, 'rx')

#plt.grid()
#plt.xlabel('zeta/m')
#plt.ylabel(' I / A')
#plt.savefig('ES1.pdf', bbox_inches='tight')

#%% Einzelspalt 2

I2, Pos2 = np.loadtxt('einzel1.txt', skiprows=1, unpack=True)

I2       = I2*1e-6 - dstr # umrechnen in Ampere
zeta2     = Pos2*1e-3
zeta2_0   = zeta2[np.argmax(I2)]
phi_2      = (zeta2 - zeta2_0)/L

plt.figure(figsize=[figwidth,figwidth])
plt.plot(zeta2, I2, 'rx')

def theory(phi, A0, b):
    return (A0 * b * np.sinc(b * np.sin(phi) / wl))**2

popt2, pcov2 = curve_fit(theory, phi_2, I2, p0 = [np.sqrt(np.max(I2)) / 1e-4, 1e-4])
print(popt2, np.sqrt(np.diag(pcov2)), sep='n')

es2_fig      = plt.figure(figsize = [10.0, 5.0])
es2_fig      = es2_fig.add_subplot(111)
linien_dicke = 1.0

x = np.linspace(-0.03, 0.03, 500)
#plt.plot(x, theory(x, *popt2)*1e6, 'y-', label='Ausgleichsrechnung')
#plt.plot(phi_2, I2*1e6, 'k.', label='Messdaten')
#plt.xlabel(r'$\varphi \,\, / \,\, \mathrm{rad}$')
#plt.ylabel(r'$I \,\, / \,\, \mu\mathrm{A}$')
#plt.legend(loc='best')
#plt.savefig('Einzelspalt2.pdf', bbox_inches='tight')

plt.figure(figsize=[figwidth,figwidth])
#plt.plot(zeta, I1, 'rx')

#plt.grid()
#plt.xlabel('zeta/m')
#plt.ylabel(' I / A')
#plt.savefig('ES1.pdf', bbox_inches='tight')

#%%Doppelspalt

I3, Pos3 = np.loadtxt('doppelvgl.txt', skiprows=1, unpack=True)

I3       = I3*1e-6 - dstr # umrechnen in Ampere
zeta3    = Pos3*1e-3      # in m
zeta3_0  = zeta3[np.argmax(I3)]
phi_3    = (zeta3 - zeta3_0)/Ld

plt.figure(figsize=[figwidth,figwidth])
plt.plot(zeta3, I3, 'rx')
#%%
# Ansatz
def I_ds(phi, A0, s, b):
    return A0**2*b**2*(4 * np.cos(np.pi * s * np.sin(phi) /wl)**2) * (np.sinc(b * np.sin(phi) / wl))**2

# Ableitung
def dI_ds(phi, s, b):
    Ids  = (4 * np.cos(np.pi * s * np.sin(phi) /wl)**2) * (np.sinc(b * np.sin(phi) / wl))**2
    z    = np.pi*np.sin(phi)/wl
    dIds = -Ids*2*np.tan(z*s)*z
    dIdb =  Ids*2*(-1/b + 1/np.tan(z*b)*z)
    return np.array([dIds, dIdb])
popt3, pcov3 = curve_fit(I_ds, phi_3, I3, p0 = [np.sqrt(np.max(I3)) / 1e-4, 4e-4, 2.9e-4])

print(popt3, np.sqrt(np.diag(pcov3)), sep='n')

ds_fig      = plt.figure(figsize = [10.5, 5.0])
ds_fig      = ds_fig.add_subplot(111)
linien_dicke = 2


#x = np.linspace(-0.004, 0.004, 100)
#plt.plot(x, I_ds(x, *popt3)*1e6, 'm-', label='Ausgleichsrechnung')
#plt.plot(phi_3, I3*1e6, 'rx', label='Messdaten')
#plt.xlabel(r'$\varphi \,\, / \,\, \mathrm{rad}$')
#plt.ylabel(r'$I \,\, / \,\, \mu\mathrm{A}$')
#plt.legend(loc='best')
#plt.savefig('doppel.pdf', bbox_inches='tight')

#%% Vergleich Überlappung von Doppelspalt und Einzelspalt

ds_fig      = plt.figure(figsize = [10.5, 9.8])
ds_fig      = ds_fig.add_subplot(111)
linien_dicke = 2

plt.plot(x, theory(x, *popt2)*1e6*4, 'k-', label='Ausgleichsrechnung Einzelspalt')
plt.plot(phi_2, I2*1e6*4, 'g.', label='Messdaten Einzelspalt')
plt.grid()
x = np.linspace(-0.009, 0.009, 100)
plt.plot(x, I_ds(x, *popt3)*1e6, 'm-', label='Ausgleichsrechnung Doppelspalt')
plt.plot(phi_3, I3*1e6, 'rx', label='Messdaten Doppelspalt')
plt.xlabel(r'$\varphi \,\, / \,\, \mathrm{rad}$')
plt.ylabel(r'$I \,\, / \,\, \mu\mathrm{A}$')
plt.legend(loc='best')
plt.savefig('VG_doppel_einzel1.pdf', bbox_inches='tight')
