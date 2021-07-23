import math 
import matplotlib.pyplot as plt 
import numpy as np 

''' calculate y = sin^2(x)  -2*pi<= x <= 2*pi'''
#xi = xmin + i∆x for i = 0; 1; 2; : : : ; n − 1:

xmin,xmax = -2*math.pi, 2*math.pi
n = 1000
x = np.linspace(xmin,xmax,n)
y1 = np.sin(x)**2
y2 = np.cos(x)**2
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()



