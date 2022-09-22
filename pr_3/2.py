with open('pr_3/logon.txt', 'r') as file:
    all = file.read().split("\n")
    for users in all:
        user = users.split(", ")
        time1 = user.split(":")
        
