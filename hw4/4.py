class Time:
    def __init__(self, sec):
        self.sec = sec
    
    def convert_to_minutes(self):
        minute = self.sec // 60
        second = self.sec % 60
        min_sec = str(minute) + ":" + str(second)
        return min_sec
    
    def convert_to_hours(self):
        hour = self.sec // 3600
        minute = (self.sec % 3600) // 60
        second = (self.sec % 3600) % 60
        hour_min = str(hour) + ':' + str(minute) + ":" + str(second)
        return hour_min

seconds = int(input())
time = Time(seconds)
print(time.convert_to_minutes())
print(time.convert_to_hours())
    