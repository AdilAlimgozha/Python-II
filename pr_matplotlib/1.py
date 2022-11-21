import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-1, 1, 100)
y = [x**2 for x in xs]

plt.plot(xs, y)
plt.show()