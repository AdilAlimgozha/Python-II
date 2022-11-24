import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def f(x):
    return pow(np.e, -x/10) * np.sin(np.pi * x)

def g(x):
    return x * pow(np.e, -x / 3)

x = np.linspace(0, 10)

plt.plot(x, f(x))
plt.plot(x, g(x))
plt.show()