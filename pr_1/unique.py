a = list(map(int, input().split()))

dict = {}

for i in range(len(a)):
    if a[i] not in dict:
        dict[a[i]] = 1
    else:
        dict[a[i]] += 1

for x in dict.keys():
    if dict[x] == 1:
        print(x)
#done