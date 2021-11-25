# The platform function
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

# The machine function
from platform import machine

print(machine())

# The processor function
from platform import processor

print(processor())

# The system function
from platform import system

print(system())

# The version function
from platform import version

print(version())

# The python_implementation and the
# python_version_tuple functions
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)