import numpy as np
from math import sqrt
from sympy import *
from math import *
import re

class Linear_alg:

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

    class Gramm_Schmidt:
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



    class SVD:
        def svd(self, A):
            self.A = np.array(A)
            self.output()

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
            y = re.sub("(\(x)|([+] x)|(- x)", "1*x", x) ##########
            y = re.sub("[a-z]||[A-Z]||\'||\=||\,||\(||\)|| ", "", y)
            z = re.split("\*", y)
            ctr = 0
            ########
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
            return self.eigvalues
        
        def D(self):
            self.D_ = np.zeros((len(self.adjAA), len(self.adjAA)))
            for i in range(len(self.eigvalues)):
                for j in range(len(self.eigvalues)):
                    if i == j:
                        self.D_[i][j] = sqrt(self.eigvalues[i])
            return self.D_

        def C(self):
            matrices_I_ref = []
            eigv_not_orth_str = []
            self.eigvec = []
            for i in range(len(self.eigvalues)):
                self.eigvalues[i] = self.eigvalues[i] * 10000000 - self.eigvalues[i]*9999999
                adjAA_minus_eigval = self.adjAA - self.eigvalues[i] * np.identity(len(self.adjAA))
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
            self.eigvec = gramm_schmidt.orthogonalization(self.eigvec)
            self.eigvec = np.array(self.eigvec)
            return self.eigvec

        def B(self):
            self.B_ = []
            eigvec_t = self.eigvec
            for i in range(len(eigvec_t)):
                if self.eigvalues[i] != 0:
                    b = np.dot(self.A, eigvec_t[i]) / sqrt(self.eigvalues[i])
                else:
                    b = np.zeros(len(self.A))
                self.B_.append(b)
            self.B_ = np.array(self.B_)
            self.B_ = np.transpose(self.B_)
            return self.B_

        def output(self):
            self.adj()
            self.find_char_pol()
            self.coefficients()
            self.D()
            self.C()
            self.B()
            print("U", self.B())
            print("D", self.D())
            print("V*", self.C())
            print(np.dot(np.dot(self.B_, self.D_), self.eigvec))


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
            return self.eigvalues

        def D(self):
            self.D_ = np.zeros((len(self.A), len(self.A)))
            for i in range(len(self.eigvalues)):
                for j in range(len(self.eigvalues)):
                    if i == j:
                        self.D_[i][j] = sqrt(self.eigvalues[i])
            return self.D_

        def C(self):
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
            self.eigvec = gramm_schmidt.orthogonalization(self.eigvec)
            self.eigvec = np.array(self.eigvec)
            return self.eigvec

        def final(self):
            DC = np.dot(np.linalg.inv(self.eigvec),self.D_)
            final = np.dot(DC,self.eigvec)
            return final

    class PD:
        def pd(self, A):
            self.A = np.array(A)
            self.output()

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
            y = re.sub("(\(x)|([+] x)|(- x)", "1*x", x) ##########
            y = re.sub("[a-z]||[A-Z]||\'||\=||\,||\(||\)|| ", "", y)
            z = re.split("\*", y)
            ctr = 0
            ########
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
            return self.eigvalues
        
        def D(self):
            self.D_ = np.zeros((len(self.adjAA), len(self.adjAA)))
            for i in range(len(self.eigvalues)):
                for j in range(len(self.eigvalues)):
                    if i == j:
                        self.D_[i][j] = sqrt(self.eigvalues[i])
            return self.D_

        def C(self):
            matrices_I_ref = []
            eigv_not_orth_str = []
            self.eigvec = []
            for i in range(len(self.eigvalues)):
                self.eigvalues[i] = self.eigvalues[i] * 10000000 - self.eigvalues[i]*9999999
                adjAA_minus_eigval = self.adjAA - self.eigvalues[i] * np.identity(len(self.adjAA))
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
            self.eigvec = gramm_schmidt.orthogonalization(self.eigvec)
            self.eigvec = np.array(self.eigvec)
            return self.eigvec

        def B(self):
            self.B_ = []
            eigvec_t = self.eigvec
            for i in range(len(eigvec_t)):
                if self.eigvalues[i] != 0:
                    b = np.dot(self.A, eigvec_t[i]) / sqrt(self.eigvalues[i])
                else:
                    b = np.zeros(len(self.A))
                self.B_.append(b)
            self.B_ = np.array(self.B_)
            self.B_ = np.transpose(self.B_)
            return self.B_

        def find_char_pol_1(self):
            M = Matrix(self.AadjA.tolist()) 
            lamda = symbols('x') 
            self.poly_1 = str(M.charpoly(lamda))
            return self.poly_1
        
        def coefficients_1(self):
            coeffs = []
            x = re.sub("\*\*\d", "", self.poly_1)
            y = re.sub("(\(x)|([+] x)|(- x)", "1*x", x) ##########
            y = re.sub("[a-z]||[A-Z]||\'||\=||\,||\(||\)|| ", "", y)
            z = re.split("\*", y)
            ctr = 0
            ########
            for coef in z:
                if coef != "":
                    coeffs.append(int(coef))
                else:
                    ctr += 1
            eigval = np.roots(coeffs)
            eig_list = eigval.tolist()
            for i in range(ctr):
                eig_list.append(0)
            self.eigvalues_1 = np.asarray(eig_list)
            self.eigvalues_1.sort()
            return self.eigvalues_1
        
        def D_1(self):
            self.D_1 = np.zeros((len(self.AadjA), len(self.AadjA)))
            for i in range(len(self.eigvalues_1)):
                for j in range(len(self.eigvalues_1)):
                    if i == j:
                        self.D_1[i][j] = sqrt(self.eigvalues_1[i])
            return self.D_1

        def C_1(self):
            matrices_I_ref = []
            eigv_not_orth_str = []
            self.eigvec_1 = []
            for i in range(len(self.eigvalues_1)):
                self.eigvalues_1[i] = self.eigvalues_1[i] * 10000000 - self.eigvalues_1[i]*9999999
                AadjA_minus_eigval = self.AadjA - self.eigvalues_1[i] * np.identity(len(self.AadjA))
                AadjA_minus_eigval_T = np.transpose(AadjA_minus_eigval)
                AadjA_minus_eigval_T_I = np.concatenate((AadjA_minus_eigval_T, np.identity(len(AadjA_minus_eigval_T))), axis = 1)
                AadjA_minus_eigval_T_I_ref = common.ref(AadjA_minus_eigval_T_I)
                AadjA_minus_eigval_Tref_Iref = np.split(AadjA_minus_eigval_T_I_ref, 2, axis = 1)
                matrices_I_ref.append(AadjA_minus_eigval_Tref_Iref[1])
            
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
                self.eigvec_1.append(s1)
            self.eigvec_1 = gramm_schmidt.orthogonalization(self.eigvec_1)
            self.eigvec_1 = np.array(self.eigvec_1)
            return self.eigvec_1

        def H(self):
            DC = np.dot(np.transpose(self.eigvec), self.D_)
            self.H_ = np.dot(DC, self.eigvec)
            return self.H_

        def U(self):
            self.U_ = np.dot(self.B_, self.eigvec)
            return self.U_

        def output(self):
            self.adj()
            self.find_char_pol()
            self.coefficients()
            self.D()
            self.C()
            self.B()
            self.find_char_pol_1()
            self.coefficients_1()
            self.D_1()
            self.C_1()
            print("H", self.H())
            print("U", self.U())
            print(np.dot(self.U(), self.H()))

    class LU:
        def multiplication_of_matrix(self, A,B):
            nrow1=len(A) 
            ncol1=len(A[0]) 
            nrow2=len(B) 
            ncol2=len(B[0]) 
            if ncol1 == nrow2:
                C = [[0 for nrow3 in range(nrow1)] for ncol3 in range(ncol2)]
                for i in range(nrow1):
                    for j in range(ncol2):
                        for k in range(nrow2):
                            C[i][j] += A[i][k]*B[k][j]
                return C

        def pivotize(self, A):
                n = len(A)
                ID = [[float(i == j) for i in range(n)] for j in range(n)]
                for j in range(n):
                    row = max(range(j, n), key=lambda i: abs(A[i][j]))
                    if j != row:
                        ID[j], ID[row] = ID[row], ID[j]
                return ID

        def lu(self, A):
                n = len(A)
                L = [[0.0] * n for i in range(n)]
                U = [[0.0] * n for i in range(n)]
                P = self.pivotize(A)
                A2 = self.multiplication_of_matrix(P, A)
                for j in range(n):
                    L[j][j] = 1.0
                    for i in range(j+1):
                        s1 = sum(U[k][j] * L[i][k] for k in range(i))
                        U[i][j] = A2[i][j] - s1
                    for i in range(j, n):
                        s2 = sum(U[k][j] * L[i][k] for k in range(j))
                        L[i][j] = (A2[i][j] - s2) / U[j][j]
                print(U)
                print(L)

linear_alg = Linear_alg
common = linear_alg.Common()
square_root = linear_alg.Square_root()

gramm_schmidt = linear_alg.Gramm_Schmidt()
svd = linear_alg.SVD()
pd = linear_alg.PD()

lu = linear_alg.LU()

print(gramm_schmidt.orthogonalization([[1,2,3], [4,5,6]]))
print()
svd.svd([[1,-2,0, 2],
        [0,1,3, 1],
        [1,0,2, 1]])
print()
pd.pd([[1,-2,0],
        [0,1,3],
        [1,0,2]])
print()
lu.lu([[1,2,3],[2,1,0],[0,0,1]])

"""square_root.square_root([[33,24],[48,57]])
square_root.find_char_pol()
square_root.coefficients()
square_root.D()
square_root.C()
print('root of A', square_root.final())"""
# square_root.square_root([[4,2,4],
#         [2,1,3],
#         [1,0,5]])
#square_root.square_root([[6,3],[2,7]])
#https://keisan.casio.com/exec/system/15076953160460
#https://www.omnicalculator.com/math/polar-decomposition