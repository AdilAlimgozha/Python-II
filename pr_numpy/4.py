import numpy as np

def nesting(a, num, ctr, lvl, d):
    if lvl not in d:
        d[lvl] = 0
    else:
        d[lvl] += ctr
    

    for i in range(len(a)):
        if a[i] == num:
            ctr+=1
            if lvl not in d:
                d[lvl] = 0
            else:
                d[lvl] += ctr
        elif type(a[i]) == list:
            return nesting(a[i], num, d[lvl], lvl+1, d)
         

a = [1, 5, 5, [5, [1, 2, 1, 1], 5, 5, 5], 5, 5, [5]]
num = 5
lst = []
d = {}
nesting(a, num, 0, 0, d)
print(d)