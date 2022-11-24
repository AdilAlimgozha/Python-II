import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 20)

y = []
for i in range(len(x)):
    if i % 2 == 0:
        y.append(x[i]*4)
    elif i % 2 != 0 and i > 60:
        y.append(x[i] * 3)
    else:
        y.append(x[i])
plt.plot(x, y, color = 'b', marker = '^')
plt.title("Title")
plt.xlabel('x')
plt.ylabel('y')
plt.show()