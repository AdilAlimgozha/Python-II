import matplotlib.pyplot as plt
import numpy as np
from pylab import *

plt.subplot(221)
plt.subplot(222)
plt.subplot(223)
plt.subplot(224)

n = 7
for i in range(10):
    x = 8000 * rand(n)
    y = 8000 * rand(n)
    area = 1000 * rand(n)
    subplot(221).scatter(x, y, s = 20, color = 'green', alpha = 1)
for i in range(10):
    x = 8000 * rand(n)
    y = 8000 * rand(n)
    area = 1000 * rand(n)
    subplot(222).scatter(x, y, s = 20, color = 'yellow', alpha = 1)
for i in range(10):
    x = 8000 * rand(n)
    y = 8000 * rand(n)
    area = 1000 * rand(n)
    subplot(223).scatter(x, y, s = 20, color = 'red', alpha = 1)
for i in range(10):
    x = 8000 * rand(n)
    y = 8000 * rand(n)
    area = 1000 * rand(n)
    subplot(224).scatter(x, y, s = 20, color = 'blue', alpha = 1)


plt.show()

plt.show()