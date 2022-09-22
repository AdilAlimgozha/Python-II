l = list(map(int, input().split()))

if l[0] + l[1] == l[2] or l[1] + l[2] == l[0] or l[0] + l[2] == l[1]:
    print("yes")
else:
    print("no")