def fac(num):
    if num == 1:
        return num
    else:
        return num*fac(num - 1)

n = int(input())
summ = 0

for i in range(3, n + 1):
    x = i * 2 * fac(i)
    summ += x

print(1 + 2 + summ)