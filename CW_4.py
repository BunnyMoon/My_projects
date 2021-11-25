#Selected functions
#from the random
#module
from random import random, seed

for i in range(5):
    print(random())

print()

seed(0)

for i in range(5):
    print(random())

print()

seed(10)

for i in range(5):
    print(random())