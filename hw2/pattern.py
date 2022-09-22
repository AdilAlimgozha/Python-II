L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
s = input()
a = []

for i in range(len(s)):
    if s[i] != "*":
        a.append([s[i], i])
print(a)

b = []
for y in L:
    for x in a:
        if y[x[1]] == x[0]:
            flag = True
            continue
        else:
            flag = False
            break
    if flag: b.append(y)

print(b)                