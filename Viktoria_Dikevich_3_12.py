#This function adds two numbers
def add(x, y):
    return x + y

#This function subtracts two numbers
def subtract(x, y):
    return x - y

#This function multiplies two numbers
def multiply(x, y):
    return x * y

#This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("Add: +")
print("Subtract: -")
print("Multiply: *")
print("Divide: /")

while True:
    choice = input("Enter choice(+ or - or * or /): ")

    #Check if choice is one of the four options
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")