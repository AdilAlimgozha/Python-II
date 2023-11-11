import numpy as np

rows_matrix_A = int(input('rows of matrix A: '))
cols_matrix_A_rows_matrix_B = int(input('cols matrix A / rows matrix B: '))
cols_matrix_B = int(input('columns of matrix B: '))

a = np.zeros((rows_matrix_A, cols_matrix_A_rows_matrix_B))
b = np.zeros((cols_matrix_A_rows_matrix_B, cols_matrix_B))

for i in range(rows_matrix_A):
    for j in range(cols_matrix_A_rows_matrix_B):
        a[i][j] = int(input('a[{i}][{j}]: '.format(i = i, j = j)))

for i in range(cols_matrix_A_rows_matrix_B):
    for j in range(cols_matrix_B):
        b[i][j] = int(input('b[{i}][{j}]: '.format(i = i, j = j)))


mult_arr = []
rows_a = len(a)
rows_b = len(b)
cols_b = len(b[0])

for i in range(rows_a):
    temp_arr = []
    for j in range(cols_b):
        sum1 = 0
        for k in range(rows_b):
            sum2 = 0
            sum2 += (a[i][k] * b[k][j])
            sum1 += sum2
        temp_arr.append(sum1)
    mult_arr.append(temp_arr)

mult_arr_np_array = np.array(mult_arr)
print(mult_arr_np_array)
        
