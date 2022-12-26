import numpy as np
from math import *

def proj_v(v, w):
    v = np.array(v)
    w = np.array(w)
    proj = ((np.dot(v, w))/(np.dot(w, w))) * w
    return proj

def orthogonalization(s_v):
    orthogonal_vectors = []
    for i in range(len(s_v)):
        if i == 0:
            orthogonal_vectors.append(s_v[0])
        elif i == 1:
            w = s_v[i] - proj_v(s_v[i], orthogonal_vectors[i - 1])
            orthogonal_vectors.append(w)
        if i >= 2:
            j = 2
            w = s_v[i] - proj_v(s_v[i], orthogonal_vectors[i - 1])
            while j != i+1:
                w = w - proj_v(s_v[i], orthogonal_vectors[i - j])
                j += 1
            orthogonal_vectors.append(w)

    summ_sq = []
    for v in orthogonal_vectors:
        summa = 0
        for el in v:
            summa += pow(el, 2)
        summ_sq.append(sqrt(summa))
    
    for i in range(len(orthogonal_vectors)):
        orthogonal_vectors[i] = (1/summ_sq[i]) * np.array(orthogonal_vectors[i])

    return orthogonal_vectors

print(orthogonalization([[2.2,2,4],[0,2,1.124214],[ 8.01019759e+07,  8.35798930e+07,  9.35758932e+07]]))