import numpy as np

def short(a):
    ctr = 0
    lst = []
    for k in range(1, 10):
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == str(k):
                    lst.append([i, j])
    for i in range(len(lst) - 1):
        ctr += abs(int(lst[i+1][0]) - int(lst[i][0])) + abs(int(lst[i+1][1]) - int(lst[i][1]))
            
    return ctr
    

a = np.array([ 
  ("00000"), 
  ("01006"), 
  ("02000"), 
  ("30050"), 
  ("00004")   ])
print(short(a))