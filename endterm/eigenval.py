import numpy as np

"""def Z5(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] >= 5:
                M[i][j] = M[i][j] % 5
    return M"""

A = np.array([[2, 4, 1],
            [1, 3, 0],
            [0, 2, 3]])
I = np.identity(3)
A_t = np.transpose(A)
adjAA = np.dot(A_t, A)
adjA_list = adjAA.tolist()

for i in range(len(adjA_list)):
    for j in range(len(adjA_list[i])):
        if i == j:
            adjA_list[i][j] = str(adjA_list[i][j]) + "-x"

char_pol = "({e00})*({e11})*({e22})+{e10}*{e21}*{e02}+{e01}*{e12}*{e20}-({e11})*{e20}*{e02}-({e00})*{e12}*{e21}-{e01}*{e10}*({e22})".format(
    e00 = adjA_list[0][0], e11 = adjA_list[1][1], e22 = adjA_list[2][2], e10 = adjA_list[1][0], e21 = adjA_list[2][1],
    e02 = adjA_list[0][2], e01 = adjA_list[0][1], e12 = adjA_list[1][2], e20 = adjA_list[2][0]
)

print(char_pol)
#print(Z5(adjAA))
#print(charac_polynom)
#print(A)
#print(I)
#print(A_t)
#print(adjAA)