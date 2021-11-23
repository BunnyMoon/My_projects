#################
#Author: Kefa   
#Date: 23.11
#Task: Fibonacci numbers(-1,25)
#################
def fibo(n):
    '''calculates Fibonacci numbers'''
    if n < 1:
         return None
    if n < 3:
        return 1

    fib1 = fib2 = 1
    sum = 0
    for i in range(3, n + 1): 
        sum = fib1 + fib2 
        fib1, fib2 = fib2, sum 
    return sum

user_num = int(input("Enter to go: "))
fibo(user_num)


for i in range(-1, 25): #testing
    print(fibo(i))