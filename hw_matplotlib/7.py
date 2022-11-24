import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import random

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
n = 250
colors = ['','cyan', 'yellow', 'purple']

for i in range(1, len(colors)):
    if i == 1:
        x = []
        for j in range(n):
            x.append(random.uniform(i, i+1.6))
        y = []
        for el in x:
            y.append(random.uniform(el - 50, el))
        z = []
        for el in x:
            z.append(random.uniform(el - 50, el + 30))
    if i == 2:
        x = []
        for j in range(n):
            x.append(random.uniform(i, i+1.6))
        y = []
        for el in x:
            y.append(random.uniform(el - 40, el + 10))
        z = []
        for el in x:
            z.append(random.uniform(el - 20, el + 40))
    if i == 3:
        x = []
        for j in range(n):
            x.append(random.uniform(i, i+1.6))
        y = []
        for el in x:
            y.append(random.uniform(el - 40, el - 20))
        z = []
        for el in x:
            z.append(random.uniform(el, el + 50))
    ax.scatter(x, y, z, color = colors[i])
plt.show()
