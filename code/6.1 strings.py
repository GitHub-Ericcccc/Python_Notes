fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

FRUIT = 'BANANAAAAA'
print(len(FRUIT))

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

# Count how many letter 'a' apperar in a word

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Slicing strings
'''
string[a:b]
: is the colon operator
slicing starts with the first number a.
The second number b is one BEYOND the end of the slice
'up to but not including'
'''
s = 'Monty Python'
print(s[0:4])
print(s[6:7])

# Notice that b is okay to beyond the length of the string
print(s[6:200])

# The use of blank a or blank b.
# From the beginning
print(s[:3])

# Till the end
print(s[3:])

# All the string
print(s[:])

# String method

stuff = 'Hello World'

# The type of an object
print(type(stuff))

# What can this object do?
print(dir(stuff))

print()  # print a blank line

print("The results above are the methods of class 'str'")

print()

print('You can use stuff.method to operate these methods')

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('HI THERE'.lower())

# The string library

print(greet.capitalize())
print(greet.center(20))
print(greet.endswith('b'))

# Return where to find the character
print(greet.find('o'))
# Return -1 if not found
print(greet.find('q'))

# There are many other string methods to use.

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('Bo', 'X')
print(nstr)

# The method REPLACE will replace ALL occurenes of the search string with the replacement string.
nstr = greet.replace('o', 'X')
print(nstr)

# NOTES: Methods get a copy of original object.


# Stripping Whitespace

greet = '   Hello Bob    '
print(greet)
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# Prefixes

line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

# Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

# The second parameter of method FIND is where the find method stars
sppos = data.find(' ', atpos)
print(sppos)

# Then slice the host address out

host = data[(atpos + 1):sppos]
print('The host address is', host)

# Take numbers from the following string.
str = 'X-DSPAM-Confidence: 0.8475'
print(str)
pos = str.find(' ')
print(pos)
piece = float(str[pos:].strip())
print(piece)
