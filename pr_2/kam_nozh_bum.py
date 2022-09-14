import random

a = ['paper', 'stone', 'scissors']
x = random.choice(a)
my = input("your: ")
print("opponent's:", x)

if x == my:
    print("nobody won")
elif x == a[0] and my == a[1] or x == a[1] and my == a[2] or x == a[2] and my == a[0]:
    print('opponent won')
else:
    print('you won')
#done