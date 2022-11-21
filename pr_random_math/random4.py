import random
import strgen

random_str = strgen.StringGenerator("[a-zA-Z]{5}").render()
print(random_str)