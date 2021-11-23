a = 1 

#Example
def fun():
    a = 2 
    print(a)


fun()
print(a)


a1 =1


def fun1():
    global a1
    a1 = 2
    print(a1)


fun1()
a1 = 3
print(a1)


a2 = 1


def fun2():
    global a2
    a2 = 2
    print(a2)

a2 = 3
fun2()
print(a2)