import numpy as np 
import matplotlib.pyplot as plt 
import random

ax,ay =[],[]

for i in range(100):
    ax.append(random.random())
    ay.append(random.random())

plt.plot(ax,ay)
plt.show()