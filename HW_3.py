#######################################################
#Author: Kefa
#Data: 02.12
#Task:to implement a class called Weeker
#######################################################


class WeekDayError(Exception): #ошибка дней недели
    pass

class Weeker:
    __weekdays = ['Mon','Tus','Wed', 'Thu','Fri','Sat', 'Sun']
    
    def __init__(self,day):
        try:
            self.__stat = self.__weekdays.index(day)
        except:
            raise WeekDayError #вызов ошибки дней недели, в случае, если нет соответсвующего дня в списке
    
    def __str__(self):
        return self.__weekdays[self.__stat]
        
    def add_days(self, n):
        '''Добавление выходных дней'''
        self.__stat = (self.__stat + n ) % 7
        
    def subtract_days(self, n):
        self.__stat = (self.__stat - n ) % 7

# test run
       
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")