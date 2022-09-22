def func(num):
    p = 1
    summ = 0
    for j in range(2, num + 1):
        for i in range(j, j + j):
            p *= j
        summ += p
    return p, summ

print(func(2))