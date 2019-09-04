import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from pylab import * 

UBr = 36*10**(-3)
f2 = 0.1491
U1 = 7
U2 = UBr/f2

k = U2/U1
print(k)