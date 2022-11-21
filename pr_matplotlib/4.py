import matplotlib.pyplot as plt
import numpy as np
from pylab import *

n = 7

colors = ['red', 'green', 'blue', 'purple', 'black', 'yellow', 'orange']
for c in colors:
    x = 1.2 * rand(n)
    y = 1.2 * rand(n)
    area = 500 * rand(n)
    plt.scatter(x, y, s = area, color = c, marker= 'o', alpha = 0.8)
plt.show()