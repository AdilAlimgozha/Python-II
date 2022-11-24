import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def f(r0, theta):
    r = r0 + np.cos(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return y
def f1(r0, theta):
    r = r0 + np.cos(theta)
    x = r * np.cos(theta)
    return x

theta = np.linspace(0, 10)

plt.plot(f1(0.8, theta), f(0.8, theta))
plt.plot(f1(1, theta), f(1, theta))
plt.plot(f1(1.2, theta), f(1.2, theta))
plt.show()