import random
import strgen

num = random.randint(6, 15)

str_random = strgen.StringGenerator("[\w]"*num).render()
a = []
for x in str_random:
    a.append(x)
sett = set(a)

str_r = ""
for x in sett:
    str_r += x
print(str_r)