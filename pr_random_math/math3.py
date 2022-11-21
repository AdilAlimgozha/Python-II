#not finished

from math import *

def E(m, n):

    vert = 0
    if n % 2 != 0 and m % 2 == 0 or n % 2 != 0 and m % 2 != 0:
        for j in range(m):
            for i in range(n):
                if j != n - 1:
                    vert += 2
                    print(i, j)
                else:
                    continue
        print(vert)
    elif n % 2 == 0 and m % 2 != 0 or n % 2 == 0 and m % 2 == 0:
        for j in range(m):
            for i in range(n):
                if j != n - 1:
                    vert += 2
                    print(i, j)
                else:
                    continue
        print(vert + (n - 1))
E(2, 2)