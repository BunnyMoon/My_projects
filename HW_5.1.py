#################
#Author: Kefa   
#Date: 23.11
#Task: to calculate factorial
#################

def factorial(n):
    '''Вычисляет факториал'''
    if n < 0:
        return None
    else:
        factor_val = 1
        for i in range(n):
            factor_val *= i+1
        return factor_val

#test code
for i in range(-1,9):
    print(factorial(i))