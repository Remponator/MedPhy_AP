import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
import pylab 
from pylab import * 

#Praxis

f = np.array([80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270])
Ubr = np.array([1090,1050,709,531,405,260,145,36,39,139,217,306,375,459,511,582,630,700,752,809])
UBr = Ubr *10**(-3)
US = np.array([7.1,7.1,7.1,7.1,7.1,7.1,7.1,7.1,7.1,7,7,7,7,7,6.95,6.95,6.95,6.95,6.95,6.95])

plt.plot(f, (UBr/US)**2, 'rx',label="Experimentelle Werte")

#Theorie

R = 1000
C = 993*10**(-9)
w0 = 1/(2*math.pi*R*C)
print(w0)
x = np.linspace(80, 270, 1000)

def A(x):
    return ((x/w0)**2-1)**2/(9*((1-(x/w0)**2)**2+9*(x/w0)**2))

plt.plot(x, A(x), 'b-',label="Theoretische Werte")

plt.xlabel('Frequenz / $Hz$')
plt.ylabel('$(U_{Br}/U_S)^2$')

plt.legend()
plt.grid()
plt.savefig('Frequenz.pdf')
plt.show()