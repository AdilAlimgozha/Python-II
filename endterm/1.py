import numpy as np
def K(x,z, p_constant=1.0):
  return (np.dot(x.T,z)+p_constant)**2
#...
x=np.array([[1, 1, 1],
            [0, 4, 0],
            [0, 0, 4]])
print(np.dot(x , np.transpose(x)))