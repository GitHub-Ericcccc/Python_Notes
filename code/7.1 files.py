# #Open a file

# File handle

# handle = open(filename,mode)
# This returns a handle to manipulate the file.

fhandle = open('/resources/mbox.txt', 'r')
# You can open, read, write and close the handle.

# handle is not the data.
print(fhandle)

# open a file that does not exist
fhandle2 = open('/resources/nothing.txt','w')

# The newline character

stuff = 'Hello\nWorld'
print(stuff)

print(len(stuff))
# The newline character \n is one character long.

# A text file has newlines at the end of each line.
# Each line is a string in the sequence.
