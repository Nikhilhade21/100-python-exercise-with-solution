'''You are given a date. Your task is to find what the day is on that date.'''

import calendar

day, month, year = map(int, input("enter:").split())
dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())