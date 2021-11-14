year = int(input("Enter a year: "))

if year < 1852: 
    print("Not within the Gregorian calendar period")
elif int(year % 4) != 0: #year isn't divisible by 4
    print("Common year")
elif int(year % 100) != 0: #year isn't divisible by 100
    print("Leap year")
elif int(year % 400) != 0: #year isn't divisible by 400
    print("Common year")
else:
    print("Leap year")