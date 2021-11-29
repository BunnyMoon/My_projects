# The in and not in
# operators

alphabet = "abcdefghiklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

print()

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#Operations on strings: 
#continued

alphabet = "bcdefghiklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

#Operations on strings: min()

print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

space = min(t)
print("is a space:", "\"", space, "\"", sep="")
print(ord(space))
print()

t = [0, 1, 2]
print(min(t))
print()

#Operations on strings: max()

print(max("aAbByYzZ"))

t1 = 'The Knights Who Say "Ni!"'
print('[' + max(t1) + ']')

t1 = [0, 1, 2]
print(max(t1))
print()

#Operations on strings: the index() method

print("aAbByYzZ".index("b"))
print("aAbByYzZ".index("Z")+1)
print("aAbByYzZ".index("A"))

# Operations on strings: the list() function

st = "abcabc"
print(st, type(st), list(st))
print()

di = {1: "1", 2: "2"}
print(di, type(di), list(di))
print()

tupl = ("1", "2")
print(tupl, type(tupl), list(tupl))
print()

#Operations on strings: the count() method

print("abcabc".count("b"))
print('abcabc'.count("d"))
print()

#The capitalize() method

print('aBcD'.capitalize())

print("Alfa".capitalize())
print("ALPHA".capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())

#The center() method

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '*') + ']')
print()

#The endswith() method

if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
print()

t3 = "zeta"
print(t3.endswith("a"))
print(t3.endswith("A"))
print(t3.endswith("et"))
print(t3.endswith("eta"))
print()

#The find() method
print("Eta".find("ta"))
print("Eta".find("mma"))
print()

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
print()

#The isalnum() meth
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('a30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print()

#The isalpha() method
#The isdigit() method
print("Mooo".isalpha())
print('Mu40'.isalpha()) 

print()

print('2018'.isdigit())
print("Year2019".isdigit())

#The islower() method
#*The isspace() method
#The isupper() method

print("Mooo".islower())
print("mooo".isalpha())

print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo". isspace())

print("Mooo".isupper())
print('moooo'.isupper())
print('MOOOOO'.isupper())
print()

#The join() method

print(",".join(["omicron", "pi", "rho"]))
print()

#The lower() method

print("SiGmA=60".lower())
print()

#The lstrip() method 
print("www.vk.com".lstrip("w."))
print("python.org".rstrip(".org"))
print()

#The replace() method
print("www.vk.com".replace("vk.com", "python.org"))
print("This is it!".replace("is", "are", 1))
print()

#The rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
print()

#The rstrip() method
print("["+ "upsilon ".rstrip() + "]")
print()

#The split() method
print("phi     chi\npsi".split())
print()

#The startswith() and strip() methods

print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

print("[" + " aleph ".strip() + "]")
print()

#The swapcase(), title(), upper() methods
print("I know that i know nothing.".swapcase())

print()

print("I know that i know nothing.".title())

print()

print("I know that i know nothing.".upper())

print()

#Examples
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

print()

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])

print()

the_list = ['Where', 'are', 'the', 'snows']
s = '*'.join(the_list)
print(s)

print()

s22 = 'It is either easy or impossible'
s22 = s22.replace('easy', 'hard').replace('im', '')
print(s22)