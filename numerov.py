from math import sqrt,pi
from scipy.optimize import fsolve
import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv
import matplotlib.pyplot as plt


#Define the potential and Energy
def v(s): return abs(s)
em = 20.

#determine grid
def f(y): return abs(y)-em
st = float(fsolve(f,em)) #findroot
ds= 1/(sqrt(2*em))
n = int(2*((st/ds)+4*pi))
s = [(-ds*(n+1)/2)+ds*i for i in range(1,n+1)]

#calculate KE matrix
def one(n,d): return np.diagflat([1 for i in range (n-abs(d))], d)
A = (one(n,-1)- 2*one(n,0) +one(n,1))/ds**2
B = (one(n,-1)+ 10*one(n,0) +one(n,1))/12.
Bi = inv(B)
K= np.matmul(-Bi, A)/2

#Hamiltonian
V= np.diagflat([v(s[i]) for i in range(n)])
H= V+K
eval, evec = eig(H)

#Denormalize the vector
evec = np.transpose(evec)

#Show the plot
plt.plot(s,evec[-20])
plt.show()
