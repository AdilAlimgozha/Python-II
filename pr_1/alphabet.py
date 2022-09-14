s = input()
al = 'abcdefghijklmnopqrstuvwxyz'
al2= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = {}
d_2 = {}

for i in range(len(al)):
    d[al[i]] = i+1

for i in range(len(al2)):
    d_2[al2[i]] = i+1

for x in s:
    if x == " ":
        print(" ", end = "")
    elif x in al:
        print(d[x], end = " ")
    else:
        print(d_2[x], end = " ")
#done