#Importing a module
from math import *
import math

print(pi)
print(e)

#Importing a module: 
#the as keyword
import math as lalala

print(lalala.pi)
print(lalala.e)


import math as m
print(m.sin(m.pi/2))

from math import pi as PI, sin as sine
print(sine(PI/2))

