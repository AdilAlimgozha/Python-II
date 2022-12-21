import numpy as np 

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
        else:
            w = s_v[i] - proj_v(s_v[i], orthogonal_vectors[i - 1])
            j = 2
            while j != i:
                w = w - proj_v(s_v[i], orthogonal_vectors[i - j])
                j += 1
            orthogonal_vectors.append(w)
    return orthogonal_vectors

print(orthogonalization([[1, 2, 4], [2, 3, 5], [4, 2, 6]]))