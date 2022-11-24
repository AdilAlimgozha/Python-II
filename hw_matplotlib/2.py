import matplotlib.pyplot as plt
import numpy as np
import random

x = [0.9, 0.016]
xl = np.linspace(0.016, 0.9, 20)
y = []
for el in xl:
    y.append(random.uniform(el - 0.1, el + 0.1))

plt.plot(x, x, color = 'r')
plt.scatter(xl, y)
plt.title("Best fit line using regression method")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()