import numpy as np

def swap(a):
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
        elif a[i] == 1:
            a[i] = 0
    return a

def freedom(a):
    ctr = 0
    print(a)
    if a[0] == 1:
        for i in range(len(a)):
            if a[i] == 1:
                ctr += 1
                swap(a)
                print(a, ctr)
    print(ctr)

a = np.array([1, 1, 0, 0, 0, 1, 0] )
freedom(a)