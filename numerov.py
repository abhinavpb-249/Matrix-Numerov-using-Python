from math import sqrt,pi
from scipy.optimize import fsolve
import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv
import matplotlib.pyplot as plt


#potential, desired max energy
def v(s): return abs(s)
em = 20.
#determine grid

def f(y): return abs(y)-em
st = float(fsolve(f,em)) #findroot
ds= 1/(sqrt(2*em))
n = int(2*((st/ds)+4*pi))
s = [(-ds*(n+1)/2)+ds*i for i in range(1,n+1)]
s=np.array(s)
#calculate KE matrix

def one(n,d): return np.diagflat([1 for i in range (n-abs(d))], d)
B = (one(n,-1)+ 10*one(n,0) +one(n,1))/12.
A = (one(n,-1)- 2*one(n,0) +one(n,1))/ds**2
Bi = inv(B)
K= np.matmul(A, -Bi)/2

V= np.diagflat([v(s[i]) for i in range(n)])
#Hamiltonian

H= V+K
eval, evec = eig(H)


i=0
while i<n:   #Denormalize the vector
    evec[:,i]= evec[:,i]/evec[:,i][-1]
    i+=1
    
evec = np.transpose(evec)

#Show the plot
plt.plot(s,evec[-20])
plt.show()
