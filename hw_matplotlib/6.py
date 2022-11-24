import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(0, 16, 100)
r = 5
x = r * np.sin(theta/2)
y = r * np.cos(theta/2)

sc_y = []
sc_z = []
for el in y:
    sc_y.append(random.uniform(el - 1, el + 1))
for el in z:
    sc_z.append(random.uniform(el - 1, el + 1))

ax.plot(x, y, z)
ax.scatter(x, sc_y, sc_z)
plt.show()
