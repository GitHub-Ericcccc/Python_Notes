
abc = 'with three words'
stuff = abc.split()
print(stuff)

print(len(stuff))
print(stuff[0])

for c in stuff:
    print(c)

# split methods by default are on whitespace
# it treats more than one space as a single space

str = 'Date 04////07/18       14:05'
stuff2 = str.split()
print(stuff2)

stuff2 = str.split('/')
print(stuff2)

# Example

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print(words[2])
#################################
# PROBLEM ABOVE REMAINS UNSOLVED.

# The double split pattern
str = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = str.split()
email = words[1]
piece = email.split('@')
hostname = piece[1]
print(hostname)