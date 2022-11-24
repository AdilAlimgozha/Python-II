import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])

vec2 = (np.pi/4) * vec1
vec2 = np.cos( vec2 )
vec3 = vec1 + 2 * vec2
la.norm(vec3)

vec4 = np.dot(mat1, vec3)
mat1_t = np.transpose(mat1)
mat1_det = np.linalg.det(mat1)
mat1_trace = np.trace(mat1)
min_v1 = np.min(vec1)
min_mat1 = np.min(mat1)

A=np.array([[17, 24, 1, 8, 15],
            [23, 5, 7, 14, 16],
            [ 4, 6, 13, 20, 22],
            [10, 12, 19, 21, 3],
            [11, 18, 25, 2, 9]])

A_T = np.transpose(A)
random_m = np.random.rand(10, 10)

m1 = []
m2 = []
m3 = []
m4 = []
m1.append(random_m[:5])
m4.append(random_m[5:])

m2.append(random_m[:5])   
m3.append(random_m[5:])

print(vec2, vec3)
print(vec4)
print(mat1_t)
print(mat1_det)
print(mat1_trace)
print(min_v1)
print(min_mat1)
for el in A:
    print(el)
    print(sum(el))
for el in A_T:
    print(el)
    print(sum(el))
print(np.diag(A))
print(sum(np.diag(A)))
print(sum(np.fliplr(A)))
print(random_m)
print(m1, m2, m3, m4)