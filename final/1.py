import numpy as np
from math import sqrt
from sympy import *
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

class SVD:
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
        self.eigenvalues_set = set(self.eigvalues)
        return self.eigvalues

        
    def D(self):
        self.D = np.zeros((len(self.adjAA), len(self.adjAA)))
        for i in range(len(self.eigvalues)):
            for j in range(len(self.eigvalues)):
                if i == j:
                    self.D[i][j] = sqrt(self.eigvalues[i])
        return self.D



    def C(self):
        matrices = []
        print(self.eigenvalues_set)
        for eival in self.eigenvalues_set:
            adjAA_minus_eigval = self.adjAA - eival * np.identity(len(self.adjAA))
            adjAA_minus_eigval_T = np.transpose(adjAA_minus_eigval)
            adjAA_minus_eigval_T_I = np.concatenate((adjAA_minus_eigval_T, np.identity(len(adjAA_minus_eigval_T))), axis = 1)
            adjAA_minus_eigval_T_I_ref = common.ref(adjAA_minus_eigval_T_I)
            #print(adjAA_minus_eigval_T_I_ref)
            adjAA_minus_eigval_Tref_Iref = np.split(adjAA_minus_eigval_T_I_ref, 2, axis = 1)
            print(adjAA_minus_eigval, eival)
        


        

    def B(self):
        if len(self.adjAA) == 3:
            self.B = []
            b1 = np.dot(self.A, self.C_t[0]) / self.D[0][0]
            b2 = np.dot(self.A, self.C_t[1]) / self.D[1][1]
            b3 = np.dot(self.A, self.C_t[2]) / self.D[2][2]
            self.B.append(b1)
            self.B.append(b2)
            self.B.append(b3)
            self.B = np.array(self.B)
            self.B = self.B.transpose()
        if len(self.adjAA) == 2:
            self.B = []
            b1 = np.dot(self.A, self.C_t[0]) / self.D[0][0]
            b2 = np.dot(self.A, self.C_t[1]) / self.D[1][1]
            self.B.append(b1)
            self.B.append(b2)
            self.B = np.array(self.B)
            self.B = self.B.transpose()
        self.matrixB = ''
        for i in range(len(self.B)):
            for j in range(len(self.B[i])):
                self.matrixB = self.matrixB + str(int(self.B[i][j])) + '    '
            self.matrixB += "\n"
        return self.matrixB
    
    def mult(self):
        self.mul = np.dot(np.dot(self.B, self.D), self.C_t)
        self.matrixmult = ''
        for i in range(len(self.mul)):
            for j in range(len(self.mul[i])):
                self.matrixmult = self.matrixmult + str(int(self.mul[i][j])) + '    '
            self.matrixmult += "\n"
        return self.matrixmult

common = Common()
svd = SVD([[1,2,3],[4,8,1],[0,7,5]])
print(svd.adj())
print(svd.find_char_pol())
print(svd.coefficients())
print(svd.D())
svd.C()
"""print(svd.B())
print(svd.mult())"""
#A = [[1,2,3,0,3],[4,8,1,2,3],[0,7,5,2,6],[1,2,5,7,9],[1,0,0,3,4]]
#print(common.determinant(A))