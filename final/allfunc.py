import random  
import numpy as np
import math
"------------------------------------Создание рандомной матрицы----------------------------------------------"
def create_matrix():
    cnt = 0
    x = int(input())
    y = int(input())
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100))
            cnt += 1  
    return array
#print(create_matrix())
"------------------------------------Сложение двух матриц----------------------------------------------"
def sum_of_matrix():
    A = create_matrix()
    B = create_matrix()
    L = []
    print(A)
    print(B)
    nrow1=len(A) 
    ncol1=len(A[0]) 
    nrow2=len(B) 
    ncol2=len(B[0]) 
    if nrow1 == nrow2 and ncol1 == ncol2: 
        for i in range(nrow1):
            l = []
            for j in range(ncol2):
                res = A[i][j] + B[i][j]
                l.append(res)
            L.append(l)
        return(L)
#print(sum_of_matrix())
"------------------------------------Разность двух матриц----------------------------------------------"
def difference_of_matrix():
    A = create_matrix()
    B = create_matrix()
    L = []
    print(A)
    print(B)
    nrow1=len(A) 
    ncol1=len(A[0]) 
    nrow2=len(B) 
    ncol2=len(B[0]) 
    if nrow1 == nrow2 and ncol1 == ncol2: 
        for i in range(nrow1):
            l = []
            for j in range(ncol2):
                res = A[i][j] - B[i][j]
                l.append(res)
            L.append(l)
        return(L)
#print(difference_of_matrix())
"----------------------------------------------Умножение двух матриц---------------------------------------------------------"
def multiplication_of_matrix():
    A = create_matrix()
    B = create_matrix()
    print(A)
    print(B)
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
#print(multiplication_of_matrix())
"--------------------------------------------------------Транспонирование матрицы-----------------------------------------------"
def transpose_of_matrix(A):
    nrow1=len(A) 
    ncol1=len(A[0]) 
    trans = [[A[j][i] for j in range(nrow1)] for i in range(ncol1)]
    return trans
#print(transpose_of_matrix(create_mattrix()))
"--------------------------------------------Ранг матрицы------------------------------------------------------"
def rank_of_matrix():
    nrow = int(input())
    ncol = int(input())
    A = np.random.randint(-100,100,size = (nrow,ncol), dtype = int)
    print(A)
    b = np.copy(A)
    cnt = 0
    Isitnull = True
    for k in range(A.shape[0]):
        if (b[k][k] == 0):
            Isitnull = False
            for i in range(k+1, A.shape[0]):
                    if (b[i][k] != 0):
                            Isitnull = True
                            b[[k]] = b[[i]] 
                            break
        if (Isitnull == False):
                break
        for i in range(k+1, A.shape[0]):
                multi = b[i][k] / b[k][k]
                for j in range(A.shape[1]):
                    b[i][j] -= multi*b[k][j]
    for i in range(A.shape[0]):
        Isitnull = False
        for j in range(A.shape[1]):
                if b[i][j] != 0:
                    Isitnull = True
        if (Isitnull == False):
            cnt+=1
    res = (A.shape[0] - cnt)
    return res
#print(rank_of_matrix())
"---------------------------------------------------Минор матрицы----------------------------------------------------"
def Minor(A,i,j):
    return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]
"------------------------------------------------Детерминант матрицы-----------------------------------------------------"
def determinant(A):
    print(A)
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    if len(A) == 3:
        return (A[0][0]*A[1][1]*A[2][2])+(A[0][1]*A[1][2]*A[2][0])+(A[0][2]*A[1][0]*A[2][1])-(A[0][2]*A[1][1]*A[2][0])-(A[0][0]*A[1][2]*A[2][1])-(A[0][1]*A[1][0]*A[2][2])
    else:
        determ = 0
        for c in range(len(A)):
            determ += ((-1)**c)*A[0][c]*determinant(Minor(A,0,c))
        return determ
#print(determinant(create_matrix()))
"----------------------------------------------Обратная матрица-----------------------------------------"
def inverse(A):
    det = determinant(A)
    if len(A) == 2:
        return [[A[1][1]/det, -1*A[0][1]/det],
                [-1*A[1][0]/det, A[0][0]/det]]
    cofactors = []
    for k in range(len(A)):
        cofactorrow = []
        for c in range(len(A)):
            minor = Minor(A,k,c)
            cofactorrow.append(((-1)**(k+c)) * determinant(minor))
        cofactors.append(cofactorrow)
    cofactors = transpose_of_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/det
    return cofactors
#print(inverse(create_matrix()))
"--------------------------------------------Собственные значения-----------------------------"
#Для 2 на 2
def eigenvalues2(A):
    print(A)
    a=int(1)
    b=0-(int(A[0][0]+A[1][1]))
    c=int(A[0][0]*A[1][1]-A[1][0]*A[0][1])
    D=b**2-4*a*c
    l1=(-b+math.sqrt(D))/(2*a)
    l2=(-b-math.sqrt(D))/(2*a)
    return l1, l2
#print(eigenvalues2(create_matrix()))

#Для 3 на 3
def eigenvalues3(A):
    print(A)
    a1 = [A[1][1],A[1][2]],[A[2][1],A[2][2]]
    a2 = [A[0][0],A[0][2]],[A[2][0],A[2][2]]
    a3 = [A[0][0],A[0][1]],[A[1][0],A[1][1]]
    M1 = determinant(a1)
    M2 = determinant(a2)
    M3 = determinant(a3)
    coeff = [1,-(A[0][0]+A[1][1]+A[2][2]), M1 + M2 + M3,-(determinant(A))] 
    sol = np.roots(coeff)
    return sol
#print(eigenvalues3(create_matrix()))