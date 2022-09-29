import re

a = []
with open('hw3/4.txt', 'r') as file:
    all = file.read().split('\n')
    for number in all:
        a.append(number)
file.close()

for i in range(len(a)):
    pattern = re.search("(((^[78]7)|(^[+]77))(\d{9}))$|(((^[87] 7)|(^[+]7 7))(\d{2} \d{3} \d{2} \d{2}))$", a[i])
    print(a[i], end = "    ")
    if pattern:
        print("YES")
    else:
        print("NO")