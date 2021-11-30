#My first class
class TheSimplestClass:
    pass
my_first_objects = TheSimplestClass()

#The stack - the procedural approach
stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
print()

#The stack - the object approach
class Stack:
    def __init__(self):
        print("Hi!")

stack_object = Stack()
print()

class Stack1:
    def __init__(self):
        self.stack_list = []

stack_object2 = Stack1()
print(len(stack_object2.stack_list))

print()

        