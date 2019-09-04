import numpy as np 

n_1, t1_1, t2_1 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/US2/Auswertung/3_1.txt', unpack=True)
n_2, t1_2, t2_2 = np.loadtxt('/Users/Remponator/Desktop/Praktikum/GitHub/Grundpraktikum/US2/Auswertung/3_2.txt', unpack=True)

c_a = 2730 #m/s
h = 8 #cm

t1_1 = t1_1*10**-6
t2_1 = t2_1*10**-6
t1_2 = t1_2*10**-6
t2_2 = t2_2*10**-6


s1_1 = (0.5*c_a*(t1_1)-0.2*10**-2)*10**2
s2_1 = (0.5*c_a*(t2_1)-0.2*10**-2)*10**2

s1_2 = (0.5*c_a*(t1_2)-0.2*10**-2)*10**2
s2_2 = (0.5*c_a*(t2_2)-0.2*10**-2)*10**2

gr_1 = s2_1 - s1_1
gr_2 = s2_2 - s1_2

print('S1_1: ',s1_1)
print('S2_1: ',s2_1)
print('S1_2: ',s1_2)
print('S2_2: ',s2_2)
print('Größe: ',gr_1,gr_2)