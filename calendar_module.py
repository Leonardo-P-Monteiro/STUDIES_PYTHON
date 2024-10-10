import calendar

# Method .calendar()

calendar_2024 = calendar.calendar(2024)
'''
Will show us a calender on terminal.
'''

# Method .month()
month_09_2024 = calendar.month(2024, 9)

'''
Will show us a month calender on terminal. 
'''

# Method .monthrange()

day_start_month, day_total_month = calendar.monthrange(2024, 9)
print(f'--> .monthrange(): Day start - {day_start_month}, Total days - \
{day_total_month}')

'''
Will return a tuple with the first day week of month start and your 
total days.
'''

# Method .weekday() with .day_name()

day_week = calendar.weekday(2024, 9, 25)
name_week_day = calendar.day_name[day_week]
print(f'--> .weekday(): {day_week}')
print(f'--> .day_name(): {name_week_day}')

# Method monthcalender()

list_calendar_month = calendar.monthcalendar(2024, 9)
list_calendar_month_enumerate = []

for week in list_calendar_month:
    for day in enumerate(week, 0):
        list_calendar_month_enumerate.append(day)

# print(list_calendar_month_enumerate)

