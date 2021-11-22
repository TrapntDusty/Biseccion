import numpy as np
import matplotlib.pyplot as plt
from math import *

fx = eval('lambda x: ' + input('Ingresa la ecuacion: '))
a = int(input("Ingresa valor a: "))
b = int(input("Ingresa valor b: "))
tolera = float(input("Ingresa la tolerancia: "))


tabla = []
tramo = b-a
fa = fx(a)
fb = fx(b)
i = 1

while (tramo>tolera):
    c = (a+b)/2
    fc = fx(c)
    tabla.append([i,a,c,b,fa,fc,fb,tramo])
    i = i + 1
                 
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia<0):
        b = c
        fb = fc
    else:
        a=c
        fa = fc
    tramo = b-a
c = (a+b)/2
fc = fx(c)
tabla.append([i,a,c,b,fa,fc,fb,tramo])
tabla = np.array(tabla)
raiz = c
np.set_printoptions(precision = 4)
print('[ i, a, c, b, f(a), f(c), f(b), tramo]')
n=len(tabla)
for i in range(0,n,1):
    unafila = tabla[i]
    formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.3f} '
    unafila = formato.format(*unafila)
    print(unafila)
print('raiz: ',raiz)

xi = tabla[:,2]
yi = tabla[:,5]
orden = np.argsort(xi)
xi = xi[orden]
yi = yi[orden]

plt.plot(xi,yi)
plt.plot(xi,yi,'o')
plt.axhline(0, color="black")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bisección en f(x)')
plt.grid()
plt.show()