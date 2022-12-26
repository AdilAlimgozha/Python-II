import numpy as np
from math import sqrt
from sympy import *
from math import *
import re

class Square_root():
    def orthogonalization(self, s_v):
        orthogonal_vectors = []
        for i in range(len(s_v)):
            if i == 0:
                orthogonal_vectors.append(s_v[0])
            elif i == 1:
                w = s_v[i] - self.proj_v(s_v[i], orthogonal_vectors[i - 1])
                orthogonal_vectors.append(w)
            if i >= 2:
                j = 2
                w = s_v[i] - self.proj_v(s_v[i], orthogonal_vectors[i - 1])
                while j != i+1:
                    w = w - self.proj_v(s_v[i], orthogonal_vectors[i - j])
                    j += 1
                orthogonal_vectors.append(w)

    def __init__(self, A):
        self.A = np.array(A)

    def adj(self):
        self.I = np.identity(len(self.A))
        self.A_t = np.transpose(self.A)
        self.adjAA = np.dot(self.A_t, self.A)
        self.AadjA = np.dot(self.A, self.A_t)
        return self.adjAA
    
    def find_char_pol(self):
        M = Matrix(self.adjAA.tolist()) 
        lamda = symbols('x') 
        self.poly = str(M.charpoly(lamda))
        return self.poly

    def coefficients(self):
        coeffs = []
        x = re.sub("\*\*\d", "", self.poly)
        y = re.sub("[a-z]||[A-Z]||\'||\=||\,||\(||\)|| ", "", x)
        z = re.split("\*", y)
        print(z)
        ctr = 0
        coeffs.append(1)
        for coef in z:
            if coef != "":
                coeffs.append(int(coef))
            else:
                ctr += 1
        print(coeffs)
        eigval = np.roots(coeffs)
        print(eigval)
        eig_list = eigval.tolist()
        for i in range(ctr):
            eig_list.append(0)
        self.eigvalues = np.asarray(eig_list)
        self.eigvalues.sort()
        return self.eigvalues    

    def C(self):
        matrices_I_ref = []
        eigv_not_orth_str = []
        eigvec = []
        for i in range(len(self.eigvalues)):
            self.eigvalues[i] = self.eigvalues[i] * 10000000 - self.eigvalues[i]*9999999
            adjAA_minus_eigval = self.adjAA - self.eigvalues[i] * np.identity(len(self.adjAA))
            adjAA_minus_eigval_T = np.transpose(adjAA_minus_eigval)
            adjAA_minus_eigval_T_I = np.concatenate((adjAA_minus_eigval_T, np.identity(len(adjAA_minus_eigval_T))), axis = 1)
            adjAA_minus_eigval_T_I_ref = Square_root.ref(adjAA_minus_eigval_T_I)
            adjAA_minus_eigval_Tref_Iref = np.split(adjAA_minus_eigval_T_I_ref, 2, axis = 1)
            matrices_I_ref.append(adjAA_minus_eigval_Tref_Iref[1])
        
        for matrix in matrices_I_ref:
            v = str(matrix[(len(matrix) - 1)])
            if (v not in eigv_not_orth_str):
                eigv_not_orth_str.append(v)
            else:
                j = 2
                while v in eigv_not_orth_str:
                    v = str(matrix[(len(matrix) - j)])
                    j += 1
                eigv_not_orth_str.append(v)
        for string in eigv_not_orth_str:
            s = re.split('\[|\]| ', string)
            s1 = []
            for i in range(len(s)):
                if s[i] != "":
                    s[i] = float(s[i])
                    s1.append(s[i])
            eigvec.append(s1)
        eigvec = Square_root.orthogonalization(eigvec)
        eigvec = np.array(eigvec)
        eigvec = eigvec.transpose()
        return eigvec

    def ref(self, A):
        r, c = A.shape
        if r == 0 or c == 0:
            return A

        for i in range(len(A)):
            if A[i,0] != 0:
                break
        else:
            B = self.ref(A[:,1:])
            return np.hstack([A[:,:1], B])
            
square_root = Square_root([[2,0,2],[0,2,0],[2, 0, -1]])
print(Square_root.adj())
print(Square_root.find_char_pol())
print(Square_root.coefficients())
print(Square_root.C())
