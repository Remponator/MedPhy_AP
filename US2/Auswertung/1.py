import numpy as np 

n, t1, t2 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/US2/Auswertung/1.txt', unpack=True)

c_a = 2730 #m/s
h = 8 #cm

t1 = t1*10**-6
t2 = t2*10**-6

s1 = (0.5*c_a*(t1)-0.2*10**-2)*10**2
s2 = (0.5*c_a*(t2)-0.2*10**-2)*10**2

print('s1: ',s1, 's2: ',s2)

gr = h-s2-s1

print('Größe: ', gr)