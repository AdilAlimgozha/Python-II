m, n = int(input()), int(input())
a = [["*"] * n for i in range(m)]


for i in range(m):
    for j in range(n):
        if i != m-1 and i != 0 and j != 0 and j != n-1 or (i == 0 or i == m - 1) and (j == 0 or j == n-1):
            a[i][j] = " "


for i in range(m):
    for j in range(n):
        print(a[i][j], end = " ")
    print()
#done