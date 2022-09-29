import re

a = []
with open('hw3/6.txt', 'r') as file:
    all = file.read().split('\n')
    for line in all:
        a.append(line)
file.close()

for line in a:
    pattern = re.search('(^[456]\d{15}$)|(^[456]\d{3}-\d{4}-\d{4}-\d{4}$)', line)
    if pattern:
        print(line, "YES")
    else:
        print(line, "NO")