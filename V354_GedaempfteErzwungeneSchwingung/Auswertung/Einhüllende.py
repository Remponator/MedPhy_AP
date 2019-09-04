import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 
from matplotlib import pylab


x = np.array([0.000040, 0.000076, 0.000116, 0.000152, 0.000192, 0.000228, 0.000268, 0.000302, 0.000338, 0.000378, 0.000418, 0.000456, 0.000494])   #Zeit
y = np.array([2.6, 1.6, 0.8, 0.2, -0.6, -1.2, -1.8, -2.2, -2.6, -3.0, -3.4, -3.6, -3.8])    #Amplitude

 
def exponenial_func(x, a, b, c):
    return a*np.exp(-b*x)+c

params, covariance = curve_fit(exponenial_func, x, y, p0=(1, 0, 0))
errors = np.diag(covariance)

print('a:', params[0], '+-', errors[0])
print('b:', params[1], '+-', errors[1])
print('c:', params[2], '+-', errors[2])

xx = np.linspace(0.000040,0.000494,1000000)
yy = exponenial_func(xx, *params)

plt.plot(x,y,'rx', xx, yy)
pylab.title('Einhüllende')
ax = plt.gca()
fig = plt.gcf()

plt.xlabel('Zeit / s')
plt.ylabel('Amplitudenspannung / V')

plt.show()

b = ufloat(3116.165753531797, 21740.140729610706) #2*pi*mu

mu = b/(2*math.pi)
print('mu:',"{:.5f}".format(mu))

L = ufloat(0.01678, 0.00009)    #Spule Literatur
R1 = 4*math.pi*L*mu                 #Widerstand : kurz vor Gleichung (4) in der Anleitung
print(R1)

R2 = ufloat()        #Widerstand Literaturwert
Tex1 = 1/b       #ausgemessen
Tex2 = 2*L/R2   #Literatur

print(Tex1)
print(Tex2)
