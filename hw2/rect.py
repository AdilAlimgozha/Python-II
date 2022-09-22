n, m = int(input()), int(input())
a = [[" "] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j ==m-1:
            a[i][j] = 'A'

for i in range(n):
    for j in range(m):
        print(a[i][j], end = " ")
    print()