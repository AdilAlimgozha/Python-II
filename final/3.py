import numpy as np

def ref(A):
    r, c = A.shape
    if r == 0 or c == 0:
        return A
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        B = ref(A[:,1:])
        return np.hstack([A[:,:1], B])

    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row
    A[0] = A[0] / A[0,0]
    A[1:] -= A[0] * A[1:,0:1]
    B = ref(A[1:,1:])
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

print(ref(np.array([[0,2,3],[4,5,6],[7,8,9]])))