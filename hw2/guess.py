import random

x = random.randint(1, 100)
print("number is", x)

while True:
    a = int(input("guess: "))
    if a > x:
        print("The number is fewer")
    elif a < x:
        print("The number is more")
    else:
        print("BINGO!")
        break