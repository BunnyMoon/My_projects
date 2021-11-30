# Instance variables
# __dict__ - names and vals each 
# vars, that an object have at the  
#time

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print()

#The inner life of 
#classes and objects
#__dict_
class Classy:
    varia =1
    def __init__(self):
        self.var = 2
    def method(self):
        pass
    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

print()

#__name__

class Classy1:
    pass

print(Classy.__name__)
obj = Classy()

#__module__
class Classy2:
    pass

print(Classy.__module__)
obj = Classy()
print(obj.__module__)

#__bases__
class SuperOne:
    pass
class SuperTwo:
    pass
class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('(', end='')

    for x in cls.__bases__:
        print(x.__name__, end='')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)