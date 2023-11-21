import matplotlib.pyplot as plt
import numpy as np

xx = np.linspace(-1, 1, 100000)
r1 = 0.1 
r2 = 0.5
r3 = 1

y11 = [(np.sqrt(r1**2 - x**2)) - 0.9 for x in xx]
y12 = [(-(np.sqrt(r1**2 - x**2))) - 0.9 for x in xx]

y21 = [(np.sqrt(r2**2 - x**2)) - 0.5 for x in xx]
y22 = [(-(np.sqrt(r2**2 - x**2))) - 0.5 for x in xx]

y31 = [(np.sqrt(r3**2 - x**2)) for x in xx]
y32 = [(-(np.sqrt(r3**2 - x**2))) for x in xx]

plt.plot(xx, y11, color = 'black')
plt.plot(xx, y12, color = 'black')
plt.plot(xx, y21, color = 'black')
plt.plot(xx, y22, color = 'black')
plt.plot(xx, y31, color = 'black')
plt.plot(xx, y32, color = 'black')
plt.show()