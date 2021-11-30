####################
#Author: Kefa
#Data: 30.11
#Task: to extend the Stack class behavior in such a 
#way so that the class is able to count all the elements 
#that are pushed and popped
###################

class Stack:
    def __init__(self):
        self.__stk = []  # Список, содержащий значения стека

    def push(self, val):
        '''Функция переносит следующие значения в стек'''
        self.__stk.append(val)

    def pop(self):
        '''Функция извлекает значеня из стека'''
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0       

    def get_counter(self):
        '''Функция возвращает "count"'''
        return self.__count

    def push(self, val):
        '''Функция  Stack.push'''
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__count += 1
        return val


# code main
if __name__ == "__main__":
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
    print(stk.get_counter()) 
