#############################################
# Author: Kefa
# Date: 21.11
# Task: write and test a function
# which takes two arguments (a year and a
# month) and returns the number of days for
# the given month/year pair
#############################################


def is_year_leap(year):
    '''Указывает на високосный год'''
    if year < 1582:
        print("Not within the Gregorian calendar period")
    elif int(year % 4) != 0:  # year isn't divisible by 4
        print("Common year")
        return False
    elif int(year % 100) != 0:  # year isn't divisible by 100
        print("Leap year")
        return True
    elif int(year % 400) != 0:  # year isn't divisible by 400
        print("Common year")
        return False
    else:
        print("Leap year")
        return True


def days_is_month(year, month):
    '''Вычисляем кол-во дней в месяце в опред. году'''
    if year < 1582 or month > 12 or month < 1:
        print("Incorrect input data")
        return None
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year) == True and month == 2:
        days_m = 29
    else:
        days_m = days[month - 1]
    print("Days in month- ", days_m, " in: ", month, "/", year)
    return days_m


test_years = [1900, 2000, 2016, 1987]
test_month = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
print("\nTEST DATA")
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_month[i]
    print(yr, "->", end="")
    result = days_is_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
