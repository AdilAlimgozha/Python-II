a = []
for i in range(3):
    a.append(list(map(int, input().split())))
print(a)
for i in range(len(a)):
    b = a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
    c = a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
    d = a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2])

print(b - c + d)
#done