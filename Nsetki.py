from math import cos, sin, pi
import random
from copy import copy


n = 1
T = 50 / (n + 1)

L = 1
h = 0.1
N_h = int(1 / h)

a = 2
tau = h / (a * 10)
N = int(T / tau)

def u0(t):
	return 0

def ul(t):
	return sin(t) / (t * t + 1)
	
def mu(x):
	return sin(pi * (n + 1) * x)
	
row1 = []
for i in range(0, N_h):
	row1.append(mu(h * i))

row1[0]= u0(0)
row1[N_h - 1] = ul(0)

alf = - a * a * tau / h**2
bet = 1 + 2 * tau  * a **2 / h**2

with open('The neyavnay scheme.xls', 'w') as fp:
    for i in range (N+1):
        t = tau * i
        row0 = copy(row1)
        row1[0] = u0(t)
        row1[N_h - 1] = round(ul(t),5)
        fp.write(str(row1[0]))
        
        A=[]
        B=[]
        A.append(0)
        B.append(0)
        
        
        for j in range(1, N_h):
            A.append(- alf / (bet + alf * A[-1]))
            B.append((row0[j] - alf * B[-1]) / (bet + alf * A[-1]))
        for j in range(N_h-2, 0, -1):
            row1[j] = round(A[j + 1] * row1[j + 1] + B[j + 1], 5)
            fp.write('\t' + str(row1[j]))
        fp.write('\t' + str(row1[N_h-1]) + '\n')
	