n = int(input())

d3 = n % 10
d2 = (n // 10) % 10
d1 = n // 100

print(d3 * 100 + d2 * 10 + d1)