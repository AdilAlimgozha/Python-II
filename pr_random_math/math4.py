from math import *
import itertools

def all_perm(n):
    global all_perm
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    all_perm = [p for p in itertools.product(numbers, repeat=n)]
    return all_perm

def number_of_repeat(a):
    ctr = 0
    all_ctr = []
    for i in range(len(a) - 1):
        if a[i] == a[i+1]:
            ctr += 1
            if i == len(a) - 2:
                all_ctr.append(ctr + 1)
        else:
            all_ctr.append(ctr + 1)
            ctr = 0
    return max(all_ctr)

def all():
    n = int(input("n = "))
    all_perm(n)
    ctr = 0
    for seq in all_perm:
        ctr += number_of_repeat(seq)
    print(ctr)

all()