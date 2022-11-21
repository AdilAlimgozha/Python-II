import random

s = input()
a = []
for x in s:
    a.append(x)

character = random.choice(a)
print(character)