import datetime

now = datetime.datetime.now()

day_of_week = now.strftime("%A")

print(f"Today is {day_of_week}")
