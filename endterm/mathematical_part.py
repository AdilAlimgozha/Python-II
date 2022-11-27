import numpy as np
from math import sqrt   #from math module was used only "sqrt"


class Common:
    def Z5(self, M): #Z5 func
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] >= 5:
                    M[i][j] = M[i][j] % 5
        return M

    def det_f(self, M): #det func
        if len(M) == 2:
            self.detM = M[1][1]*M[0][0] - M[1][0]*M[0][1]
        elif len(M) == 3:
            b = M[0][0] * (M[1][1] * M[2][2] - M[2][1] * M[1][2])
            c = M[1][0] * (M[0][1] * M[2][2] - M[2][1] * M[0][2])
            d = M[2][0] * (M[0][1] * M[1][2] - M[1][1] * M[0][2])
            self.detM = b - c + d
        return self.detM

    def char_pol_f(self, M, x): #characteristic polinomyal func
        if len(M) == 2:
            self.char_p = (M[0][0] - x) * (M[1][1] - x) - M[0][1] * M[1][0]
        elif len(M) == 3:
            b = (M[0][0] - x) * ((M[1][1] - x) * (M[2][2] - x) - M[2][1] * M[1][2])
            c = M[1][0] * (M[0][1] * (M[2][2] - x) - M[2][1] * M[0][2])
            d = M[2][0] * (M[0][1] * M[1][2] - (M[1][1] - x) * M[0][2])
            self.char_p = b - c + d
        return self.char_p

class SVD:
    def __init__(self, A):
        self.A = A

    def D(self):
        self.I = np.identity(len(self.A))
        self.A_t = np.transpose(self.A)
        self.adjAA = np.dot(self.A_t, self.A)
        common.Z5(self.adjAA)
        self.adjAA_list = self.adjAA.tolist()

        self.eigenvalues = []    #finding eigenvalues
        if len(self.adjAA) == 3:
            for i in range(5):
                if common.char_pol_f(self.adjAA, i) == 0:
                    self.eigenvalues.append(i)
            if len(self.eigenvalues) == 1:
                x1, x2, x3 = self.eigenvalues[0], self.eigenvalues[0], self.eigenvalues[0]
            elif len(self.eigenvalues) == 3:
                x1, x2, x3= self.eigenvalues[0], self.eigenvalues[1], self.eigenvalues[2]
            elif len(self.eigenvalues) == 2:
                x1, x2 = self.eigenvalues[0], self.eigenvalues[1]
                if common.char_pol_f(self.adjAA, x1+0.1) > 0 and common.char_pol_f(self.adjAA, x1 - 0.1) > 0 or common.char_pol_f(self.adjAA, x1+0.1) < 0 and common.char_pol_f(self.adjAA, x1 - 0.1) < 0:
                    x3 = x1
                elif common.char_pol_f(self.adjAA, x2+0.1) > 0 and common.char_pol_f(self.adjAA, x2 - 0.1) > 0 or common.char_pol_f(self.adjAA, x2+0.1) < 0 and common.char_pol_f(self.adjAA, x2 - 0.1) < 0:
                    x3 = x2
            all_eigval = [x1, x2, x3]
        elif len(self.adjAA) == 2:
            for i in range(5):
                if common.char_pol_f(self.adjAA, i) == 0:
                    self.eigenvalues.append(i)
            if len(self.eigenvalues) == 1:
                x1, x2 = self.eigenvalues[0], self.eigenvalues[0]
            elif len(self.eigenvalues) == 2:
                x1, x2 = self.eigenvalues[0], self.eigenvalues[1]
            all_eigval = [x1, x2]

        self.D = np.zeros((len(self.adjAA), len(self.adjAA)))
        for i in range(len(all_eigval)):
            for j in range(len(all_eigval)):
                if i == j:
                    self.D[i][j] = sqrt(all_eigval[i])
        common.Z5(self.D)
        print(self.D)

        for i in range(len(self.adjAA_list)):   #str characteristic polinomyal
            for j in range(len(self.adjAA_list[i])):
                if i == j:
                    self.adjAA_list[i][j] = str(self.adjAA_list[i][j]) + "-x"
        if len(self.adjAA) == 3:
            self.char_pol_str = "({e00})*({e11})*({e22})+({e10})*({e21})*({e02})+({e01})*({e12})*({e20})-({e11})*({e20})*({e02})-({e00})*({e12})*({e21})-({e01})*({e10})*({e22})".format(
                e00 = self.adjAA_list[0][0], e11 = self.adjAA_list[1][1], e22 = self.adjAA_list[2][2], e10 = self.adjAA_list[1][0], e21 = self.adjAA_list[2][1],
                e02 = self.adjAA_list[0][2], e01 = self.adjAA_list[0][1], e12 = self.adjAA_list[1][2], e20 = self.adjAA_list[2][0])
        elif len(self.adjAA) == 2:
            self.char_pol_str = "({e00})*({e11}) - ({e01})*({e10}))".format(e00 = self.adjAA_list[0][0], e11 = self.adjAA_list[1][1],
            e01 = self.adjAA_list[0][1], e10 = self.adjAA_list[1][0])
        print(self.char_pol_str)

    #def B(self):



common = Common()
svd = SVD(np.array([[0, 2, 0],
                [0, 0, -3],
                [1, 0, 0]]))
svd.D()