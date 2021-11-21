####################
# Author: Kefa
# Date: 21.11
# Task: Simple Calculator by Using Functions
####################

def add(x, y):
    '''Суммирует два числа'''
    print(x, "+", y, "=", x + y)


def subtract(x, y):
    '''Вычисляет разницу'''
    print(x, "-", y, "=", x - y)


def multiply(x, y):
    '''Умножение двух чисел'''
    print(x, "*", y, "=", x * y)


def divide(x, y):
    '''Деление двух чисел'''
    print(x, "/", y, "=", x / y)


def max_min(x, y):
    print("Max:", max(x, y),"\nMin:", min(x, y))




while True:
    print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Max|min\nEnter 'exit' to close the program")
    choice = input("Enter choice (1/2/3/4/'exit'): ")

    if choice in ("1", "2", "3", "4", "5"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "1":
            add(x, y)

        elif choice == "2":
           subtract(x, y)

        elif choice == "3":
            multiply(x, y)

        elif choice == "4":
            divide(x, y)

        elif choice == "5":
            max_min(y, x)

        elif choice == "exit":
            break

        # Выбор действий после вывода ответа
        next_calculation = input("Let's do next calculation? (yes/exit): ")
        if next_calculation == "exit":
            break
    else:
        print("Invalid Input")
