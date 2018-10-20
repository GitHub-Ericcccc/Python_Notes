# processing files

# A file handle open for read can be treated as a sequence of strings
# where each line in the file is a string in the sequence
# We can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set

# Read the file line by line (TYPE ONE)
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

# Line counting
count = 0
for line in xfile:
    count = count + 1
print('Line Count:', count)

# Read the whole file (TYPE TWO)
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[0:30])

# Search through a file
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)

# The result may have blank lines between desired outcomes.
# This is because PRINT FUNCTION will add a \n newline everytime it runs.
# However, the text file has \n newline at the end of each line!
# This results two \n \n getting too many blank lines.

# To deal with this extra newline problem, we use attribute lstrip, rstrip or strip.

fhand = open('mbox.txt')
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        print(line)


# Skip undesired line with Continue

fhand2 = open('mbox.txt')
for line in fhand2:
    line = line.strip()
    if not line.startswith('From'):
        continue
    print(line)
# By doing this you can get exactly the same outcome.

# Using in

fhand3 = open('mbox.txt')
for line in fhand3:
    line = line.strip()
    if not 'uct' in line:
        continue
    print(line)


# Bad file names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit() # The quit() statement will quit this code, avoiding proceed to the 'for-loop' below.

count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There are', count, 'subject lines in', fname)