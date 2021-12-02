#######################################################
#Author: Kefa
#Data: 02.12
#Task:Create Pizza class to make pizza
#######################################################


class Pizza():
    def __init__(self, pizza=[]):
        self.__pizza_list = pizza

    def make_pizza_class(self, pz, ch):
        if pz not in  self.__pizza_list: 
            raise PizzaError(pz, "no such pizza in menu") 
        if ch >100:
            raise  TooMuchCheeseError(pizza = pz, cheese = ch, message="too much cheese")
        print("Pizza ready!") 
    


class PizzaError(Exception):
   def __init__(self, pizza='UNKNOWN', message = ''):
      Exception.__init__(self, message)
      self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uncknown', cheese = '>100 G', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

## process start
pizza_obj = Pizza(pizza = ['margherita','capricciosa','calzone'])

for (pz, ch) in [('calzone', 0),('margherita', 110), ('mafia', 20)]:
   try:
      pizza_obj.make_pizza_class(pz, ch)
   except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese,)
        
   except PizzaError  as  pe:
        print(pe.pizza,"- ", pe)