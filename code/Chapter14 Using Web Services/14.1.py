# 14.2

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed.')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
              print('I amd destructed', self.x)

x = PartyAnimal()

x.party()
x.party()
x.party()
x = 546165 # assign new value to x and destruct its class
print('x contains', x)

print(dir(PartyAnimal)) # Notice that there is 'party' and 'x' inside which defined by this class.


# What we are doing here is just like
# For example the class 'list'
# newlist = list()
# newlist.append('x')
# newlist.append('x')
# newlist.append('x')
# print(newlist)

# append is a method (inner function) of the object list
# the 'x' here is the data of the object list
# the newlist is an oject of class list


class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed.')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal('sally')
s.party()

j = PartyAnimal('jim')
j.party()
s.party()

# This example works like this:
# s = {x=2, name = sally}
# j = (x=1, name = jim)
# s and j are two independent instances with their own name and x.


#14.4 Object Inheritance
print('#14.4 Object Inheritance')

# Make a new class by reusing an existing class and inherit all the capabilities of the existing one and then modify it to make new class.
# The new class (child) has all the capabilities of the old class (parent) - and then some more.
# Subclasses are more specialized versions of a class, which INHERIT attributes and behaviors from their parent classes and can introduce their own.

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed.')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

# Now class FootballFan has three vairables and three methods.

s = PartyAnimal('sally')
s.party()

j = FootballFan('jim')
j.party()
j.touchdown()
