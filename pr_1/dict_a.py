import re
d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'Todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'Helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'},
]

for dict in d:
    x = re.search(".8$", dict['phone'])
    if x:
        print(dict['name'])
#done