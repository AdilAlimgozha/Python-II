import random
import strgen

str_random = strgen.StringGenerator("[\d]{4}[a-zA-Z0-9]{6}").render()

lst = []
for x in str_random:
    lst.append(x)

rand = random.sample(lst, k = 10)
s = ""
for x in rand:
    s += x
print(s)