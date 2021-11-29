# Strings - a brief review

#Example 1
word = 'by'
print(len(word))

#Example 2

empty = ''
print(len(empty))

#Example 3

i_am = 'I\'m'
print(len(i_am))

#Multiline strings

multiline = '''Line #1
Line #2'''

print(len(multiline))

multiline1 = """Line #1
Line #2"""

print(len(multiline1))

#Operations on strings
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#Operations on strings: 
#ord()
#Ex1

char_1 = 'a'
char_2 = ' ' #space
print(ord(char_1))
print(ord(char_2))

#Operations on strings: chr()
print(chr(97))
print(chr(945))

#Strings as sequences: 
#indexing

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#2
the_string1 = 'silly walks'

for ix in range(len(the_string1)-1, -1, -1):
    print(the_string1[ix], end=' ')

print()

#Strings as sequences: 
#iteratin
the_string2 = 'silly walks'

for character in the_string2:
    print(character, end='\n')

print()

#Slices 

alpha = "abdefd"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

