import re

with open('hw3/3.txt', 'r') as file:
    words = file.read().split()
    punct = ".,!?"
    a = []
    for word in words:
        for letter in word:
            if letter in punct:
                word = word[:len(word) - 1]
        a.append(word)
file.close()

for word in a:
    ime = re.search('ime$', word)
    if ime:
        print("a)", word)

for word in a:   
    ave = re.search('.{1}ave', word)
    if ave:
        print("b)", word)

ctr = 0
for word in a:
    rstlne = re.search("r|s|t|l|n|e|R|S|T|L|N|E", word)
    if rstlne:
        ctr += 1
print("c)", ctr)

ctr = 0
for word in a:
    rstln = re.search("r|s|t|l|n|R|S|T|L|N", word)
    if rstln:
        ctr += 1
print("d)", str(ctr / len(a) * 100) + "%")

for word in a:
    vowels = re.search("[aeiouyAEIOUY]", word)
    if vowels:
        print("", end = "")
    else:
        print("e)", word)

for word in a:
    d = {}
    vowels = re.findall("[aeiouy]", word)
    vowels = set(vowels)
    if len(vowels) == 6:
        print("f)", word)
