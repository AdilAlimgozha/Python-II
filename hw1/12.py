x = int(input("Input first number:"))
y = int(input("Input second number:"))
z = int(input("Input third number:"))

a = [x, y, z]
maxi = max(a)
mini = min(a)
for i in range(3):
    if a[i] != maxi and a[i] != mini:
        print(a[i])
#done