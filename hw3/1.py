with open('hw3/students.txt', 'r') as file:
    students = file.read().split('\n')
    a = []
    for student in students:
        each = student.split(' ')
        each[0] = each[0].capitalize()
        each[1] = each[1].capitalize()
        each[3] = '301-' + each[3]
        a.append(each)
file.close()

with open('hw3/students2.txt', 'w') as file:
    students2 = ""
    for i in range(len(a)):
        for ea in a[i]:
            students2 = students2 + ea + ' '
        if i != len(a) - 1:
            students2 = students2.strip() + '\n'
        else:
            students2 = students2.strip()
    file.write(students2)
file.close()