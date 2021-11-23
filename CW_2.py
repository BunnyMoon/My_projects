#global nonlocal
def my_function():
    global var
    var = 2
    print("Do i know that variable?", var)


var = 1
my_function()
print(var)