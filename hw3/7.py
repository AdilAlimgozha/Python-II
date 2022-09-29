import re
import string
a = []                          # take from file
with open('hw3/7.txt', 'r') as file:
    all = file.read().split('\n')
    for line in all:
        a.append(line)
file.close()

c = []                        # remove punctuation and split
for x in a:
    splitted_line = re.split('\,+\s+|\.+|\,+|\s+', x)
    c.append(splitted_line)

dates = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sen", "Oct", "Nov", "Dec"]
dates_low = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sen", "oct", "nov", "dec"]

for i in range(len(c)):         #converting
    for j in range(12):
        date = re.search('(^{datename})|(^{datename_low})'.format(datename = dates[j], datename_low = dates_low[j]), c[i][0])
        if date:
            print(str(j+1) + "/" + c[i][1] + "/" + c[i][2][2:])