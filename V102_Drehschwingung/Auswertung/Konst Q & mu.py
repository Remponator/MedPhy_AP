import numpy as np 
import scipy.constants as const
import math
from uncertainties import ufloat

E = ufloat(21*10**10, 0.05*10**10)
G = ufloat(167811943904.27, 10060136619.25)

def mu(E, G):
    return E/(2*G) - 1

def Q(E, mu):
    return E/(3*(1-2*mu(E,G)))

print(mu(E,G))
print(Q(E,mu))