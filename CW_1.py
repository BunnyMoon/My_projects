try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeeded!")
except:
    print("We failed")
print("We're done")

print()

try:
    print("appha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexError:
    print("index")
except:
    print("some")

print()

# Exceptions: continue
try:
     y = 1/0
except ZeroDivisionError:
    print("Ooooppppsss....")

print('THE END.')

try:
    y = 1/ 0
except ArithmeticError:
    print("Oooopppss...2")

print("THE END.2")
print()
# Exceptions: continue
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
bad_fun(0)

print("THE END.")

def bad_fun1(n):
    return 1 / n

try:
    bad_fun1(0)
except ArithmeticError:
    print("What happend? An exception\
was raised") 
    
print("THE END.")

print()

# Exceptions: continued

def bad_fun2(n):
    raise ZeroDivisionError

try:
    bad_fun2(0)
except ArithmeticError:
    print("What happend? An error?")

print("THE END.")

print()

# Exceptions: continued

def bad_fun3(n):
    try:
        return n / 0
    except: 
        print("I did it again!")

try:
    bad_fun3(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

#Exceptions: continued

import math 

x = float(input("Enter a nuumber: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)





