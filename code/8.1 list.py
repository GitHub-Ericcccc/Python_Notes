print('hello world')

list1 = ['a', 'b', 'c']
list2 = [22, 33, 44]
list3 = ['xyz', list1, list2]
list4 = []
list0 = [list1, list2, list3, list4]

# print(list1)
# print(list2)
# print(list3)
# print(list4)

for listx in list0:
    print(listx)

# Strings are immutable, you can not change a string.
# Lists are mutable, you can change an element of a list using index operator.

nstr = 'banana'
# nstr[2] = x will return you a traceback.
# but you can use attribute of a string to get a copy.
nstr = nstr.upper()
print(nstr)

list1[1] = 55
print(list1)

# compare the length of a string and a list.
print('The length of nstr is ', str(len(nstr)).strip(), '.')
print('The lenght of list1 is ', str(len(list1)).strip(), '.')

# qustion: how to delete the blankspace after the length number.

# Range Function
# The range function returns the successive items of the desired sequence.
# It returns a class 'range', and a class is an object.
# This sequence behaves like a list of numbers that range from zero to one less than the parameter.
# However, it is not a list.
# We can construct an index loop using 'for' and an inter iterator.

range(4)
print(range(4))
print(list(range(4)))
friends = ['a', 'b', 'c']
print('The length is ', len(friends))
print('The range is ', range(len(friends)))

# Use range to construct lists

for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i] # use index operator
    print('Happy New Year:', friend)

# These two sets of code do exactly the same thing.
# By using range function, you do not have to wirte like this:
# for i in [0:x], where you need x at the first place.

