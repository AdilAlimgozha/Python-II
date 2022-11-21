import random

tickets = []

for i in range(100):
    str_num = ''
    for j in range(10):
        num = random.randint(1, 9)
        str_num += str(num)
    if str_num not in tickets:
        tickets.append(int(str_num))
    else:
        str_num = ''
        for j in range(10):
            num = random.randint(1, 9)
            str_num += str(num)
print(tickets)
win = random.sample(tickets, k = 2)
print(win)