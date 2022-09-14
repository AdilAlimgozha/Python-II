months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = int(input())
day = int(input())

name = months[month - 1]
if 1 <= month <= 2 or month == 12:
    season = "Season is winter"
elif 3 <= month <= 5:
    season = "Season is spring"
elif 6 <= month <= 8:
    season = "Season is summer"
elif 9 <= month <= 11:
    season = "Season is autumn"

print(name, day, season)
#done