import matplotlib.pyplot as plt 
import numpy as np 

# The data - lists of years:
year = [1972, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 1999, 2000, 2003,2004, 2007, 2008, 2012]
# And number of transistors (ntrans) on CPUs in millions:
ntrans = [0.0025, 0.005, 0.029, 0.12, 0.275, 1.18, 3.1, 7.5, 24.0, 42.0, 220.0, 592.0, 1720.0, 2046.0, 3100.0]

ntrans = np.array(ntrans)*1.e6
n0,y0 = ntrans[0],year[0]
y = np.linspace(y0,year[-1],year[-1]-y0+1)
T2 =2

mr = np.log10(n0)+(y-y0)/T2*np.log10(2)

plt.plot(year,np.log10(ntrans),"*",label='observed',markersize =12,markeredgecolor='r',color='r')
plt.plot(y,mr,label='predicted',markersize =12,markeredgecolor='r',color='k',ls='--',lw=2)
plt.legend(fontsize =16,loc ='upper left')
plt.xlabel('year')
plt.ylabel('log(ntrans)')
plt.title('Moors law')
plt.show()