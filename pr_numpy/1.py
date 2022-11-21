import numpy as np

a = np.array([(2, 2, 3, 6),
             (4, 5, 6, 5), 
             (7, 8, 2, 24), 
             (12,15,18,45)])
a_t = a.transpose()

print(a)

for i in range(len(a)):
    for j in range(len(a_t)):
        summ = sum(a[i][:len(a) - 1])
        summ_t = sum(a_t[j][:len(a_t) - 1])
        if a[i][len(a_t) - 1] != summ and a_t[j][len(a) - 1] != summ_t:
            if a[i][len(a_t) - 1] - summ + a[i][j] == a[3][j] - summ_t + a[i][j]:
                print('wrong:', a[i][j])
                a[i][j] = a[i][len(a_t) - 1] - summ + a[i][j]
                print(a)
            else:
                print('wrong:', a[i][j], a[len(a) - 1][j])
                a[i][j] = a[i][len(a_t) - 1] - summ + a[i][j]
                a_t[j][i] = a[i][j]
                summ_t = summ_t = sum(a_t[j][:len(a_t) - 1])
                a[len(a) - 1][j] = summ_t
                print(a)
        elif a[i][len(a_t) - 1] != summ and a_t[j][len(a) - 1] == summ_t:
            print("wrong:", a[i][len(a_t) - 1])
            a[i][len(a_t) - 1] = summ
            print(a)
        elif a[i][len(a_t) - 1] == summ and a_t[j][len(a) - 1] != summ_t:
            print("wrong:", a_t[j][len(a) - 1])
            a[len(a) - 1][j] = summ_t
            print(a)