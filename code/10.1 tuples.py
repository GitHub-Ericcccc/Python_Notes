
# Tuples are a limited version of list.
# It is more efficient but you cannot modify.

x = ('aaa', 'bbbb', 'ccccc')
print(x[0])
print(x)
print(max(x))

# Tuples are not mutable.

x = [2, 3, 6]
print(x)
x[1] = 5
print(x)

# y = ('aaa', 'bbbb', 'ccccc')
# y[0] = 'd'
# TypeError: 'tuple' object does not support item assignment.

# You cannot sort, append, reverse a tuple.

l = list()
t = tuple()

print(dir(l))
print(dir(t))

# When we are making temporary variables, we prefer tuples over lists.

# Tuples and assignment
# We can put a tuple on the LEFT_HAND SIDE of an assignment statement.
# We can even OMIT the parentheses.

(x, y) = (4, 'fed')
print(x, y)
print(y)
# This means x = 4 and y = 'fed'

(a, b) = (99, 98)
print((a, b))
print(a, b)

# The items() method in dictionaries returns a list of (key, value) tuples.

d = dict()
d['a'] = 2
d['b'] = 4
for k, v in d.items():
    print(k, v)

d = dict()
d['a'] = 2
d['b'] = 4
tups = d.items()
print(tups)

# The result is a list of tuples.
# dict_items([('a', 2), ('b', 4)])
# This is how a two-tuples list works in two-iteration loop.

# Tuples are comparable.

print((1, 2, 3) < (2, 2, 3))
print((0, 1, 20000) < (0, 3, -1))
print(('john', 'sally') < ('john', 'sam'))
# The result is TRUE because john = john, sa = sa, l < m.

print(('jones', 'sally') > ('adams', 'sam'))
# The result is TRUE beacuse j > a, it never looks the second item.

# Conclusion: tuples are sortable by their first items.
# If the first items match, then looks to the next.

d = {'a': 19, 'c': 1, 'b': 22}

print(d.items())

# sort by key order
print(sorted(d.items()))

# sort by value order

d = {'a': 19, 'c': 1, 'b': 22}
print(d)
tmp = list()
for k, v in d.items():
    tmp.append((v, k))

print(tmp)

tmp = sorted(tmp, reverse=True)
# You can get sorted list of tuples from big value to small.
print(tmp)


# Find the ten most common words

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split() # list of words
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # counts = {word: number}

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
    # lst = {number: word}

lst = sorted(lst, reverse=True)
# lst = {numberbig: word, ..., numbersmall: word}

for val, key in lst[:10]:
# {num1st: word, num2nd: word: ..., num10th: word}
    print(key, val)
    # (word number)


# Simplify the code above.
# Take in dictionary and output with a list of sorted tuples.

# List comprehension SHORTER VERSION OF CODE ABOVE.
c = {'a': 10, 'b': 1, 'c': 22}
print(c)
print(sorted([ (v, k) for k, v in c.items() ], reverse=True))

# List comprehension creates a dynamic list.
# We make a list of reversed tuples and then sort it.
# Here, we made from dictionary into sorted list of tuples.
