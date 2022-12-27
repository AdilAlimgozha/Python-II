import numpy as np
from math import sqrt
from sympy import *
from math import *
import re


class Common:

    def Minor(self, A, i, j):
        return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]

    def determinant(self, A):
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return A[0][0]*A[1][1]-A[0][1]*A[1][0]
        if len(A) == 3:
            return (A[0][0]*A[1][1]*A[2][2])+(A[0][1]*A[1][2]*A[2][0])+(A[0][2]*A[1][0]*A[2][1])-(A[0][2]*A[1][1]*A[2][0])-(A[0][0]*A[1][2]*A[2][1])-(A[0][1]*A[1][0]*A[2][2])
        else:
            self.determ = 0
            for c in range(len(A)):
                self.determ += ((-1)**c)*A[0][c] * self.determinant(self.Minor(A,0,c))
            return self.determ
    
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

        if i > 0:
            ith_row = A[i].copy()
            A[i] = A[0]
            A[0] = ith_row
        A[0] = A[0] / A[0,0]
        A[1:] -= A[0] * A[1:,0:1]
        B = self.ref(A[1:,1:])
        return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

    def proj_v(self, v, w):
        v = np.array(v)
        w = np.array(w)
        proj = ((np.dot(v, w))/(np.dot(w, w))) * w
        return proj

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

        summ_sq = []
        for v in orthogonal_vectors:
            summa = 0
            for el in v:
                summa += pow(el, 2)
            summ_sq.append(sqrt(summa))
        
        for i in range(len(orthogonal_vectors)):
            orthogonal_vectors[i] = (1/summ_sq[i]) * np.array(orthogonal_vectors[i])

        return orthogonal_vectors



class Square_root:
    def square_root(self, A):
        self.A = np.array(A)
        return self.A

    def find_char_pol(self):
        M = Matrix(self.A.tolist()) 
        lamda = symbols('x') 
        self.poly = str(M.charpoly(lamda))
        return self.poly
    
    def coefficients(self):
        coeffs = []
        x = re.sub("\*\*\d", "", self.poly)
        y = re.sub("[a-z]||[A-Z]||\'||\=||\,||\(||\)|| ", "", x)
        z = re.split("\*", y)
        ctr = 0
        coeffs.append(1)
        try:    
            for coef in z:
                if coef != "":
                    coeffs.append(int(coef))
                else:
                    ctr += 1
            eigval = np.roots(coeffs)
            eig_list = eigval.tolist()
            for i in range(ctr):
                eig_list.append(0)
            self.eigvalues = np.asarray(eig_list)
            self.eigvalues.sort()
        except:
            return "Square root for this matrix is not defined"
        return self.eigvalues

    def D(self):
        try:
            self.D_ = np.zeros((len(self.A), len(self.A)))
            for i in range(len(self.eigvalues)):
                for j in range(len(self.eigvalues)):
                    if i == j:
                        self.D_[i][j] = sqrt(self.eigvalues[i])
        except:
            return 
        return self.D_

    def C(self):
        try:
            matrices_I_ref = []
            eigv_not_orth_str = []
            self.eigvec = []
            for i in range(len(self.eigvalues)):
                self.eigvalues[i] = self.eigvalues[i] * 10000000 - self.eigvalues[i]*9999999
                adjAA_minus_eigval = self.A - self.eigvalues[i] * np.identity(len(self.A))
                adjAA_minus_eigval_T = np.transpose(adjAA_minus_eigval)
                adjAA_minus_eigval_T_I = np.concatenate((adjAA_minus_eigval_T, np.identity(len(adjAA_minus_eigval_T))), axis = 1)
                adjAA_minus_eigval_T_I_ref = common.ref(adjAA_minus_eigval_T_I)
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
                self.eigvec.append(s1)
            self.eigvec = common.orthogonalization(self.eigvec)
            self.eigvec = np.array(self.eigvec)
        except:"Square root for this matrix is not defined"

        return self.eigvec

    def final(self):
        try:
            DC = np.dot(np.linalg.inv(self.eigvec),self.D_)
            final = np.dot(DC,self.eigvec)
        except:
            return "Square root for this matrix is not defined"
        return final


common = Common()
square_root = Square_root()
# square_root.square_root([[4,2,4],[2,1,3],[1,0,5]])
# square_root.square_root([[6,3],[2,7]])
#square_root.square_root([[1,3,-3],[0,4,5],[0,0,9]])
#square_root.square_root([[1,2,2],[0,1,1,],[0,-1,2]])
print(square_root.find_char_pol())
print()
print(square_root.coefficients())
print()
print(square_root.D())
print()
print(square_root.C())
print()
print(square_root.final())