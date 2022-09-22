s = "evaporate"
s1 = "_" * len(s)

while True:
    lett = input("Guess your letter: ")
    if lett in s1:
        print("you already have this letter")
    for i in range(len(s)):
        if lett == s[i]:
            s1 = s1[:i] + lett + s1[i + 1:]
    if lett not in s:
        print("incorrect")
    print(s1)
    if s == s1:
        print("you won!")
        break