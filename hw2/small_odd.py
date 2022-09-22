a = [int(input()) for i in range(6)]
a1 = []

for i in range(6):
    if a[i] % 2 != 0:
        a1.append(a[i])

if len(a1) != 0:
    print(min(a1))
else:
    print("not found")