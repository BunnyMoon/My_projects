#############################################
# Author: Kefa
# Date: 21.11
# Task: to write and test a function
# which takes one argument (a year) and
# returns True if the year is a leap year, or
# False otherwise.
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


year = int(input("Enter year: "))
print(is_year_leap(year))

# test code
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end=" ")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
