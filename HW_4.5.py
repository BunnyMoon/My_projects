#############################################
# Author: Kefa
# Date: 21.11
# Task: find prime numbers
#############################################

def is_prime(x):
    '''Поиск простого числа'''
    if x == 1:
        return False
    else:
        for a in range(2, x):
            if x % a == 0:
                return False
    return True


for i in range(1, 20):# Поиск простых чисел в определённом диапазоне
    if is_prime(i+1):
        print(i + 1, end=" ")
print()


