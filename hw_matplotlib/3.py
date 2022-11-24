import matplotlib.pyplot as plt
import numpy as np
from math import *

x = np.linspace(0, 50, 100)
y = np.sin(x / 7.95)
z = -np.sin(x / 7.95)
h = np.cos(x / 7.95)
g = -np.cos(x / 7.95)

plt.plot(x, y, color = 'b')
plt.plot(x, z, color = 'g')
plt.plot(x, h, color = 'orange')
plt.plot(x, g, color = 'r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()