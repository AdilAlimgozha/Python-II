import random as r

ctr = 0
while True:
    if ctr == 3:
        break
    x = r.randint(100, 999)
    if x % 5 == 0:
        ctr += 1
        print(x)