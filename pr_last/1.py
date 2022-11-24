import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

x = 10
xsq = pow(x, 2)
xqb = pow(x, 3)
theta = 90
sinn = np.degrees(np.sin(theta))
coss = np.degrees(np.cos(theta))

meshPoints = np.linspace(-1, 1, 500)
meshP_56 = meshPoints[55]
print(meshP_56)
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()