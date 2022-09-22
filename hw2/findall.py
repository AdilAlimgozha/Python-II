def findall(string, letter):
    list_index = []
    for i in range(len(string)):
        if string[i] == letter:
            list_index.append(i)
    return list_index

s, lett = input(), input()
print(findall(s, lett))