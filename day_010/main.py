# Task - Days in month
# Task 3 - Leap Year
def is_leap(year):
    lap_year = False
    if year % 4 == 0:
        lap_year = True
        if year % 100 == 0:
            lap_year = False
            if year % 400 == 0:
                lap_year = True
    return lap_year

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    if month != 2:
        return month_days[month-1]
    else:
        if is_leap(year):
            return 29
        else:
            return 28

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = days_in_month(year, month)
print(days)