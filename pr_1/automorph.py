def automorph(number):
    N = number * number
    for i in range(1, len(str(N)) + 1):
        mod = N % (pow(10, i))
        if number == mod:
            return number #True or number


n = int(input())
a = []
for i in range(1, n):
    if automorph(i):
        a.append(i)

print(a)
#done