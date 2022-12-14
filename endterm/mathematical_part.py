import numpy as np
from math import sqrt   #from math module was used only "sqrt"


class Common:
    def Z5(self, M): #Z5 func
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] >= 5 or M[i][j] < 0:
                    M[i][j] = M[i][j] % 5
        return M

    def det_f(self, M): #det func
        if len(M) == 2:
            self.detM = (M[1][1]*M[0][0] - M[1][0]*M[0][1]) % 5
        elif len(M) == 3:
            b = M[0][0] * (M[1][1] * M[2][2] - M[2][1] * M[1][2])
            c = M[1][0] * (M[0][1] * M[2][2] - M[2][1] * M[0][2])
            d = M[2][0] * (M[0][1] * M[1][2] - M[1][1] * M[0][2])
            self.detM = (b - c + d) % 5
        return self.detM

    def char_pol_f(self, M, x): #characteristic polinomyal func
        if len(M) == 2:
            self.char_p = pow(x, 2)-self.trace(M)*x+self.det_f(M)
        elif len(M) == 3:
            self.char_p = pow(x, 3)-self.trace(M)*pow(x, 2)+self.sum_of_minors_3(M)*x-self.det_f(M)
        return self.char_p
    
    def trace(self, M):
        if len(M) == 2:
            self.trac = (M[0][0] + M[1][1]) % 5
        elif len(M) == 3:
            self.trac = (M[0][0] + M[1][1] + M[2][2]) % 5
        return self.trac

    def sum_of_minors_3(self, M):
        m1 = self.det_f(np.array([[M[0][0], M[0][1]],[M[1][0], M[1][1]]]))
        m2 = self.det_f(np.array([[M[0][0], M[0][2]],[M[2][0], M[2][2]]]))
        m3 = self.det_f(np.array([[M[1][1], M[1][2]],[M[2][1], M[2][2]]]))
        self.sum_minors = (m1 + m2 + m3) % 5
        return self.sum_minors
    
    def eigenvectors_3(self, M, x, y, z):
        return M[0][0] * x + M[0][1] * y + M[0][2] * z, M[1][0] * x + M[1][1] * y + M[1][2] * z, M[2][0] * x + M[2][1] * y + M[2][2] * z

    def eigenvectors_2(self, M, x, y):
        return M[0][0] * x + M[0][1] * y, M[1][0] * x + M[1][1] * y
    
    def existance_solution(self):
        return False

class SVD:
    def __init__(self, A):
        self.A = A

    def adj(self):
        self.I = np.identity(len(self.A))
        self.A_t = np.transpose(self.A)
        self.adjAA = np.dot(self.A_t, self.A)
        common.Z5(self.adjAA)

        self.matrixadjAA = ''
        for i in range(len(self.adjAA)):
            for j in range(len(self.adjAA[i])):
                self.matrixadjAA = self.matrixadjAA + str(int(self.adjAA[i][j])) + '    '
            self.matrixadjAA += "\n"
        return self.matrixadjAA

    def find_eigenvalues(self):
        self.eigenvalues = []    #finding eigenvalues
        if len(self.adjAA) == 3:
            for i in range(5):
                if common.char_pol_f(self.adjAA, i) % 5 == 0:
                    self.eigenvalues.append(i)
            if len(self.eigenvalues) == 0:
                return common.existance_solution()
            if len(self.eigenvalues) == 1:
                x1, x2, x3 = self.eigenvalues[0], self.eigenvalues[0], self.eigenvalues[0]
            elif len(self.eigenvalues) == 3:
                x1, x2, x3= self.eigenvalues[0], self.eigenvalues[1], self.eigenvalues[2]
            elif len(self.eigenvalues) == 2:
                x1, x2 = self.eigenvalues[0], self.eigenvalues[1]
                if common.char_pol_f(self.adjAA, x1+0.1) > 0 and common.char_pol_f(self.adjAA, x1 - 0.1) > 0 or common.char_pol_f(self.adjAA, x1+0.1) < 0 and common.char_pol_f(self.adjAA, x1 - 0.1) < 0:
                    x1, x2, x3 = x2, x1, x1
                elif common.char_pol_f(self.adjAA, x2+0.1) > 0 and common.char_pol_f(self.adjAA, x2 - 0.1) > 0 or common.char_pol_f(self.adjAA, x2+0.1) < 0 and common.char_pol_f(self.adjAA, x2 - 0.1) < 0:
                    x3 = x2
            self.all_eigval = [x1, x2, x3]
        elif len(self.adjAA) == 2:
            for i in range(5):
                if common.char_pol_f(self.adjAA, i) == 0:
                    self.eigenvalues.append(i)
            if len(self.eigenvalues) == 0:
                    return common.existance_solution()
            if len(self.eigenvalues) == 1:
                x1, x2 = self.eigenvalues[0], self.eigenvalues[0]
            elif len(self.eigenvalues) == 2:
                x1, x2 = self.eigenvalues[0], self.eigenvalues[1]
            self.all_eigval = [x1, x2]
        if 0 in self.all_eigval:
            return common.existance_solution()
        self.matrixEVAL = ""
        for i in range(len(self.all_eigval)):
            self.matrixEVAL = self.matrixEVAL + str(int(self.all_eigval[i])) + '    '
        return self.matrixEVAL

    def D(self):
        self.D = np.zeros((len(self.adjAA), len(self.adjAA)))
        for i in range(len(self.all_eigval)):
            for j in range(len(self.all_eigval)):
                if i == j:
                    self.D[i][j] = sqrt(self.all_eigval[i])
        common.Z5(self.D)

        self.matrixD = ''
        for i in range(len(self.D)):
            for j in range(len(self.D[i])):
                self.matrixD = self.matrixD + str(int(self.D[i][j])) + '    '
            self.matrixD += "\n"
        return self.matrixD

    def str_charac_pol(self):   #str characteristic polinomyal
        if len(self.adjAA) == 3:
            self.char_pol_str = "x^3 - {trace}x^2 + {mins}x - {det} = 0".format(trace = common.trace(self.adjAA), mins = common.sum_of_minors_3(self.adjAA), det = common.det_f(self.adjAA))
        elif len(self.adjAA) == 2:
            self.char_pol_str = "x^2 - {trace}x + {det} = 0".format(trace = common.trace(self.adjAA), det = common.det_f(self.adjAA))
        return self.char_pol_str

    def C(self):
        matrices_eigvec = []
        for x in self.all_eigval:
            mat_eig = self.adjAA - x * np.identity(len(self.adjAA))
            common.Z5(mat_eig)
            matrices_eigvec.append(mat_eig)
            eigenvec = []
            if len(self.adjAA) == 3:
                for m in range(len(matrices_eigvec)):
                    vectors = []
                    for i in range(5):
                        for j in range(5):
                            for k in range(5):
                                if common.eigenvectors_3(matrices_eigvec[m], i, j, k)[0] % 5 == 0 and common.eigenvectors_3(matrices_eigvec[m], i, j, k)[1] % 5 == 0 and common.eigenvectors_3(matrices_eigvec[m], i, j, k)[2] % 5 == 0:
                                    vectors.append([i, j, k])
                    eigenvec.append(vectors)
                for i in range(len(eigenvec)):
                    if len(eigenvec[i]) > 1:
                        if i == 0:
                            eigenvec[i] = [1, 0, 0]
                        if i == 1:
                            eigenvec[i] = [0, 1, 0]
                        if i == 2:
                            eigenvec[i] = [0, 0, 1]
                    else:
                        eigenvec[i] = eigenvec[i][0]
                self.C_t = np.array(eigenvec)
                common.Z5(self.C_t)
                self.C = self.C_t.transpose()
            elif len(self.adjAA) == 2:
                for m in range(len(matrices_eigvec)):
                    vectors = []
                    for i in range(5):
                        for j in range(5):
                                if common.eigenvectors_2(matrices_eigvec[m], i, j)[0] % 5 == 0 and common.eigenvectors_2(matrices_eigvec[m], i, j)[1] % 5 == 0:
                                        vectors.append([i, j])
                    eigenvec.append(vectors)
                for i in range(len(eigenvec)):
                    if len(eigenvec[i]) > 1:
                        if i == 0:
                            eigenvec[i] = [1, 0]
                        if i == 1:
                            eigenvec[i] = [0, 1]
                    else:
                        eigenvec[i] = eigenvec[i][0]
                self.C_t = np.array(eigenvec)
                common.Z5(self.C_t)
                self.C = self.C_t.transpose()
        self.matrixC_t = ''
        for i in range(len(self.C_t)):
            for j in range(len(self.C_t[i])):
                self.matrixC_t = self.matrixC_t + str(int(self.C_t[i][j])) + '    '
            self.matrixC_t += "\n"
        return self.matrixC_t

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
            common.Z5(self.B)
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
"""svd = SVD([[0, 2, 1],
                [0, 0, 2],
                [1, 0, 0]])
print(svd.adj())
print(svd.find_eigenvalues())
print(svd.str_charac_pol())
print(svd.D())
print(svd.C())
print(svd.B())
print(svd.mult())"""