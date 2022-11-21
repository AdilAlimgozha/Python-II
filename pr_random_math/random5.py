import random
import strgen

password = strgen.StringGenerator("[A-Z]{2}[\d]{1}[\W]{1}[\w]{6}").render()
a = []
for x in password:
    a.append(x)

perm = random.sample(a, k = 10)

password1 = ""
for x in perm:
    password1 += x

print(password1)