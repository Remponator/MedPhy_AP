import numpy as np 

n = 8
t = 9.6

f = t/n*60 #Puls

V = (0.25*1484*(53.5**(-6))+0.02)*np.pi*0.05**2

L1 = V/0.001 * 1000 #ml

ESV = 2/3*np.pi*(0.05**3) - V

L2 = ESV/0.001 * 1000 #ml

print('EDV: ',L1)
print('ESV: ',L2)