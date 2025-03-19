# We use classes to bundle data and functionality into one unit.
# Sometimes you will come across classes that don't have any behaviour, they don't have any methods
# They only have data, here is an example
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2) # False -> because both objects are stored in different locations in memory
# So by default python compares objects based on where they are stored in memory
# if two variables are referencing the same object in memory they are considered equal
# id()  <-- this built-in funct returns address of the memory location
# print(id(p1))
# print(id(p2))

# Writing all these code for data classes is tedious i.e. (tasks that require a lot of effort)
# If you're dealing with classes that have no behaviour, no methods, they only have data you can use a
# "namedtuple" instead
# from collections module import namedtuple funct

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])  #we want our Point object to have 2 attributes
# namedtuple  arguments:
# first argument -> name for the new type we wanna create
# 2nd argument -> an array of attribute names
# this funct returns a namedtuple that we can store I used Pascal naming convention i.e. Point =
# since Point here represent a type like a class
# calling it to create a new Point object
p1 = Point(x=1, y=2)  # pass keyword arguments
p2 = Point(x=1, y=2)
# Now we don't need any magic method to compare two objects
print(p1 == p2)


# So if you're working with classes that only have data and no methods you might wanna use namedtuple
# instead, you will write less code
# here we have the attributes in the point object just like the attributes we've in our classes
print(p1.x)
# These namedtuple are immutable, once created cannot be modified





