def dig(n):
    d3 = n % 10
    d2 = (n // 10) % 10
    d1 = n // 100
    return pow(d1, 3) + pow(d2, 3) + pow(d3, 3)

for i in range(100, 1000):
    if dig(i) == i:
        print(i, end = " ")