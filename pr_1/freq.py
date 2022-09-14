a = list(map(int, input().split()))

dict = {}

for i in range(len(a)):
    if a[i] not in dict:
        dict[a[i]] = 1
    else:
        dict[a[i]] += 1

max = (max(dict.values()))

for x in dict.keys():
    if dict[x] == max:
        print(x)
#done