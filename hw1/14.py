a = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        a.append(x)

summ = float(sum(a))
print(summ / len(a))
#done