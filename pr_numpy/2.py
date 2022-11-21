import numpy as np

def can_see(mat, maxt_tr):
    flag = True
    for i in range(len(maxt_tr)):
        for j in range(len(mat[i]) - 1):
            if maxt_tr[i][j] >= maxt_tr[i][j+1]:
                flag = False
                break

    if flag:
        print('yes')
    else:
        print('no')

a = np.array([[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]])
a_t = a.transpose()
can_see(a, a_t)