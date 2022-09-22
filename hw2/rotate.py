a = input().split()

for i in reversed(range(len(a)-1)):
    temp = a[i]
    a[i] = a[i + 1]
    a[i + 1] = temp

print(a)