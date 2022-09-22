with open("pr_3/score.txt", "r") as file:
    all = file.read().split("\n")
    a = []
    for stud in all:
        each = stud.split(" ")
        new_score = int(each[1]) + 5
        a.append([each[0], str(new_score)])
file.close()

with open("pr_3/score_2.txt", "w") as file:
    for stud in a:
        s = stud[0] + " " + stud[1] + "\n"
        file.write(s)
#done