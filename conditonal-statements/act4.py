import datetime
import calendar

time_now = datetime.datetime.now()
print("Time right now : ", time_now)

year = int(input("Enter year : "))
print(f"Entire Calendar for {year}....")
print(calendar.calendar(year))