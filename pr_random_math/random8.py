import random
import strgen

num = random.randint(6, 15)
password = strgen.StringGenerator("[\W]"*num).render()

print(password)