import numpy as np 

#Kathodentemperatur
I_f = np.array([2,2.1,2.2,2.3,2.5]) #Heizstrom in A
U_f = np.array([4,4.5,4.8,5.0,6.0]) #Heizspannung in V

k_b = 1.3806488e-23 #Boltzmankonst.
e_0 = 1.602e-19 #Coulomb

def T(I_f,U_f):
    return ((U_f*I_f-1)/(5.7e-12*0.32))**0.25 #Wärmeleitung N=1W

print('Temp. Glühdraht: ',T(I_f,U_f))

#Teil e) - Austrittsarbeit
h = 6.626e-34 #Plank.const
m_0 = 9.109e-31 #Elektronmasse

I_s = np.array([0.161,0.368,0.781,1.353,3])*10**(-3) #I in A

#Austrittsarbeit in eV
W_A = (-np.log((I_s*h**3)/(e_0*m_0*k_b**2*T(I_f,U_f)**2))*k_b*T(I_f,U_f))/e_0

W_A_m = np.mean(W_A)
err_W_A = np.std(W_A, ddof=1) / np.sqrt(len(W_A))

print('Austrittsarbeit: ',W_A)
print('Mittelwert Austrittsarbeit: ',W_A_m,err_W_A)