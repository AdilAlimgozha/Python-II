human = int(input("Input a dog's age in human years: "))
if human < 3:
    print(human * 10.5)
else:
    print("The dog's age in dog's years is", int((human - 2) * 4 + 10.5 * 2))
#done