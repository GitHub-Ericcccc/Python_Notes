import re

fhand1 = open('42.txt') # test file
fhand2 = open('72.txt') # actual file

count = 0
numsum = 0

for line in fhand2:
    line = line.strip() # delete whitespace
    wordlist = line.split() # split one line string into a list of each word
    if re.findall('[0-9]+', line): # find any numbers contained in each word
        #count = count + 1 # number counting
        numlst = re.findall('[0-9]+', line) # give the list of num
        for numstr in numlst:
            num = int(numstr) # convey the number(str) into number(int)
            numsum = numsum + num # sum them up
            print(num) #print the number found in one word
            count = count +1

print(count)
print(numsum)
