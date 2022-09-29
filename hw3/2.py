with open('hw3/2_1.txt', 'r') as file:
    lines = file.read().split('\n')
    a = []
    for line in lines:
        a.append(line)
file.close()

with open('hw3/2_2.txt', 'r') as file:
    lines = file.read().split('\n')
    b = []
    for line in lines:
        b.append(line)
file.close()

with open('hw3/2_3.txt', 'w') as file:
    for i in range(len(a)):
        for j in range(len(b)):
            if i != len(a) - 1 and j != len(b) - 1:
                if i == j:
                    together = a[i] + " " + b[j] + '\n'
            else:
                if i == j:
                    together = a[i] + " " + b[j]
        file.write(together)
file.close()