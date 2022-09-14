months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = input()

for i in range(len(months)):
    if months[i] == month:
        index = i+1

if index == 2:
    print("28/29 days")
if index <= 7:
    if index % 2 != 0:
        print("31 days")
    else:
        if index != 2:
            print("30 days")
else:
    if index % 2 != 0:
        print("30 days")
    else:
        print("31 days")
#done