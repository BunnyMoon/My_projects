from sys import path
path.append("..\\packages\\")
from packages.mysplit import mysplit

print(mysplit.split("To be or not to be, that is the question"))
print(mysplit.split("To be or not to be,that is the question"))
print(mysplit.split("   "))
print(mysplit.split("abc"))
print(mysplit.split(""))