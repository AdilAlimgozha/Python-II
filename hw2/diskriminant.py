from math import *
a, b, c = int(input()), int(input()), int(input())

D = b * b - 4 * a * c

if D < 0:
    print('no roots')
elif D == 0:
    x = -b / 2 * a
    print(x)
else:
    x1 = (-b + sqrt(D))/2 * a
    x2 = (-b - sqrt(D))/2 * a
    print(x1, x2)