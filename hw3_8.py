import re

with open('hw3_8.txt', 'r') as file:
    a = []
    all = file.read().split('\n')
    for line in all:
        a.append(line)
print(a)

name = input()

for fullname in a:
    if len(name) == 2:
        initial = re.search('^{letter1}.*{letter2}'.format(letter1 = name[0], letter2 = name[1]), fullname)
    elif len(name) == 3:
        initial = re.search('^{letter1}.*{letter2}'.format(letter1 = name[0], letter2 = name[2]), fullname)
    if initial:
        print(fullname)
#done