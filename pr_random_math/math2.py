from math import *

def check_triangle_exists(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True

def check(a, b, c):
    if a <= b <= c:
        return True

def check_int_median(a, b, c):
    m = sqrt(2 * pow(a, 2) + 2 * pow(b, 2) - pow(c, 2))/2
    if m.is_integer():
        return True

n = int(input("n = "))
ctr = 0
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if check_triangle_exists(i, j, k) and check_int_median(i, j, k) and check(i, j, k):
                ctr += 1

print(ctr)