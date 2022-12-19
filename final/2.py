import numpy as np 
a = np.array([[1, 2, 4], [3, 4, 5], [5, 6 ,7]])
b = np.identity(len(a))

q = np.concatenate((a, b), axis=1)
print(q)
print(np.split(q ,2, axis = 1))