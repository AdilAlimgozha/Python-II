import numpy as np 
import math
A = np.array([[13,7,4],
             [7,9,-3],
             [4,-3,9]])
def zeros_matrix(n):
    l=[]
    for i in range(n):
        l1=[]
        for j in range(n):
            l1.append(0)
        l.append(l1)
    return np.array(l)
def choljj(j):
    X=A[j,j]
    l=[]
    for k in range(j):
        X=X-L[j,k]**2
    return math.sqrt(X)
def cholij(i,j):
    X=A[i,j]
    for k in range(j):
        X=X-L[i,k]*L[j,k]
    return X
def transpose_of_matrix(A):
    nrow1=len(A) 
    ncol1=len(A[0]) 
    trans = [[A[j][i] for j in range(nrow1)] for i in range(ncol1)]
    return trans
def Cholesky_decomposition(A):
    size = len(A)
    L = zeros_matrix(size).astype(float)   
    for i in range(size):
        for j in range(size):
            if i==j and i==0:
                L[i,j]=math.sqrt(A[i,j])
            elif j==0:
                L[i,0] = A[i,0]/L[0,0]
            elif i==j and j>=1:
                L[j,j]=choljj(j)
            elif i>=j:
                L[i,j]=cholij(i,j)/L[j,j]     
    return L

print(Cholesky_decomposition(A))