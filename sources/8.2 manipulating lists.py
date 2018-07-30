# Concatenating Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a, b, c)

# Slicing lists
t = [1, 3, 5, 7, 9]
t1 = t[1:3]
t2 = t[:4]
t3 = t[-3:]
t4 = t[:]

print(t, t1, t2, t3, t4)

# List Methods
x = list()
print(type(x))
print(dir(x))

# Building a list from scratch
stuff = list()
print(stuff)
stuff.append(99)
print(stuff)
stuff.append('x')
print(stuff)
# Lists are mutable, so you can use .append
# append will add at the end of list.

some = [1,3,5,7,9]
print(9 in some)
print(2 in some)
print(18 not in some)

# sorting lists
friends = ['Allen', 'Eric', 'Bob', 'Cristin']
print(friends)
friends.sort()
print(friends)

# Built-in functions and lists
nums = [32,5,3,73,5,43]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# Two ways to product average
# Type One

total = 0
count = 0
while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count +1
average1 = total / count
print(average1)

# Type Two

numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average2 = sum(numlist)/len(numlist)
print(average2)

# One tiny difference of this two types.
# Type one has only two numbers at the same time
# Type two has all numbers in the memory, which may use much memory space.
