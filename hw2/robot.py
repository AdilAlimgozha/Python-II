from math import *
a = []
for i in range(4):
    x = tuple(input().split())
    a.append(x)

s_h = 0
s_w = 0

for x in a:
    if "UP" in x:
        s_h += int(x[1])
    elif "DOWN" in x:
        s_h -= int(x[1])
    if "LEFT" in x:
        s_w += int(x[1])
    elif "RIGHT" in x:
        s_w -= int(x[1])

print(s_h, s_w)

print(round(sqrt(pow(s_h, 2) + pow(s_w, 2))))