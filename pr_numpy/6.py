import numpy as np

def repl(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == '-':
                a[i][j] = '0'
    return a

def mines(a):
    repl(a)
    for i in range(len(a) - 1):
        for j in range(len(a[i]) - 1):
            """if a[0][0] == '#':
                if a[i+1][j] != '#': a[i+1][j] = str(int(a[i+1][j]) + 1)
                if a[i+1][j+1] != '#': a[i+1][j+1] = str(int(a[i+1][j+1]) + 1)
                if a[i][j+1] != '#': a[i][j+1] = str(int(a[i][j + 1]) + 1)
            if a[0][len(a[i]) - 1] == '#':
                if a[i+1][j] != '#': a[i+1][j] = str(int(a[i+1][j]) + 1)
                if a[i+1][j-1] != '#': a[i+1][j-1] = str(int(a[i+1][j-1]) + 1)
                if a[i][j-1] != '#': a[i][j-1] = str(int(a[i][j - 1]) + 1)
            if a[len(a) - 1][0] == '#':
                if a[i][j+1] != '#': a[i][j+1] = str(int(a[i][j + 1]) + 1)
                if a[i-1][j] != '#': a[i-1][j] = str(int(a[i-1][j]) + 1)
                if a[i-1][j+1] != '#': a[i-1][j+1] = str(int(a[i-1][j+1]) + 1)
            if a[len(a) - 1][len(a[i]) - 1] == '#':
                if a[i][j-1] != '#': a[i][j-1] = str(int(a[i][j - 1]) + 1)
                if a[i-1][j] != '#': a[i-1][j] = str(int(a[i-1][j]) + 1)
                if a[i-1][j-1] != '#': a[i-1][j-1] = str(int(a[i-1][j-1]) + 1)"""
            
            if a[i][j] == '#':
                a[i+1][j] = str(int(a[i+1][j]) + 1)
                a[i+1][j+1] = str(int(a[i+1][j+1]) + 1)
                a[i+1][j-1] = str(int(a[i+1][j-1]) + 1)

                a[i][j+1] = str(int(a[i][j + 1]) + 1)
                a[i][j-1] = str(int(a[i][j - 1]) + 1)

                a[i-1][j] = str(int(a[i-1][j]) + 1)
                a[i-1][j+1] = str(int(a[i-1][j+1]) + 1)
                a[i-1][j-1] = str(int(a[i-1][j-1]) + 1)
            if a[i][j + 1] == '#':
                a[i+1][j+1] = str(int(a[i+1][j]) + 1)
                a[i+1][j] = str(int(a[i+1][j-1]) + 1)

                a[i][j] = str(int(a[i][j - 1]) + 1)

                a[i-1][j+1] = str(int(a[i-1][j]) + 1)
                a[i-1][j] = str(int(a[i-1][j-1]) + 1)

            
    return a

a = np.array([ 
  ["#", "-", "-", "-", "#"], 
  ["-", "-", "-", "-", "-"], 
  ["-", "-", "#", "-", "-"], 
  ["-", "-", "-", "-", "-"], 
  ["-", "-", "-", "-", "-"]])

print(mines(a))