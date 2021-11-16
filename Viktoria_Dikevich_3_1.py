# Read four numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
number4 = float(input("Enter the fourth number: "))


#Choose the larger number
if number1 > number2:
    larger_number = number1
elif number2 > number3:
    larger_number = number2
elif number3 < number4:
    larger_number = number4
#if the user entered the same numbers
elif number3 == number4:
    print("The third and fourth numbers have the same value")
else:
    larger_number = number3
print("The larger number is:", larger_number, type(larger_number))

    
    



