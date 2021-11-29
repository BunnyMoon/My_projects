# AssertionError
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that anngle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
print()

#KeyboardInterrupt

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")

#OverflowError

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
except OverflowError:
    print('The number is too big.')

#ImportError

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')