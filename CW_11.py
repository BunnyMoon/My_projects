#recursion
def factorial_function(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return factorial_function(n-1) + factorial_function(n-2)


for n in range (1, 10):
    print(n, "->", factorial_function(n))