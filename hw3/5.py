import re

a = []
with open('hw3/5.txt', 'r') as file:
    all = file.read().split('\n')
    for line in all:
        each = line.split(' <')
        each[1] = each[1][:len(each[1]) - 1]
        a.append(each)
file.close()

b = []
for line in a:
    email = re.search('.+@.+[.][a-z]', line[1])
    if email:
        b.append(line)

for element in b:
    print(element[0], element[1])