import datetime

year = int(input())
month = int(input())
day = int(input())

x = datetime.datetime(year, month, day) + datetime.timedelta(days = 1)
print(x.strftime('%Y-%m-%d'))
#done