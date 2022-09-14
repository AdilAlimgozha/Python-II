vowel = "aeiouy"

letter = input("Input a letter of the alphabet: ")
if letter not in vowel:
    print(letter, "is consonant")
else:
    print(letter, "is vowel")
#done