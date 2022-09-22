n = int(input())

d3 = n % 10
d2 = (n // 10) % 10
d1 = n // 100

if d1 < d2 < d3:
    print("yes")
else:
    print("no")