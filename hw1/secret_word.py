secret_message = input()
count_of_groups = int(input())
a = ["" for i in range(count_of_groups)]

for i in range(count_of_groups):
    #print("group {}:".format(i+1), end = " ")  the second way to solve
    for j in range(i, len(secret_message), count_of_groups):
        a[i] += secret_message[j]
        #print(secret_message[j], end = " ") the second way to solve
    print("group {}:".format(i+1), a[i])



#decoder
max = 0
do_readable = ""
for i in range(len(a)):
    do_readable += a[i]
    if  len(a[i]) > max:
        max = len(a[i])
for i in range(max):
    for j in range(count_of_groups):
        if i < len(a[j]):
            print(a[j][i], end = "")
#done