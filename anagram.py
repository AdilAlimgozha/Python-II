to = list(input())
fromm = list(input())
flag = True
a = []

for i in range(len(to)):
    for j in range(len(fromm)):
        if to[i] == fromm[j]:
            a.append(j)
            to[i] = " "
            fromm[j] = " "
            break

a.sort()
for i in range(len(a) - 1):
    if a[i] + 1 != a[i + 1]:
        flag = False

if flag:
    print("yes")
else:
    print("no")