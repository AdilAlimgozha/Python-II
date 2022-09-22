n = int(input())

d4 = n % 10
d3 = (n // 10) % 10
d2 = (n // 100) % 10
d1 = n // 1000

rev_n = d4 * 1000 + d3 * 100 + d2 * 10 + d1

if n == rev_n:
    print("yes")
else:
    print("no")


"""
s = input()
s1 = ""

for x in reversed(s):
    s1 += x

if s1 == s:
    print("yes")
else:
    print("no")
"""