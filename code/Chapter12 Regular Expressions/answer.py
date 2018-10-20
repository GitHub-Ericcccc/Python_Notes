import re

#Extracting Digits and Summing them
hand = open("72.txt")
numlist = []
count = 0
for line in hand:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        print(num)
        numlist.append(num)
        count = count +1

print(sum(numlist))
print(count)
