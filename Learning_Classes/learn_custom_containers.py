# Earlier we learnt about lists, sets, dictionaries and so on...
# These data structures or container types are pretty useful and sufficient for most cases.
# But there are times when you want to create your own custom container types
# Various operations around containers: len() of the container
# get an item by its key. eg: persons["name"],  we can also set that eg: persons["name"] = "Jo"
# We can iterate over the container eg: for person in persons
# These are some of the operations that we are going to implement in our custom container.
# Here I am using dictionary
# {'python': 3}  <-- Here 'python' is my key and '3' is the value of that key
# here what I am doing is, if my key doesn't exist in the dict set its value to 1, if it exists increment its value by 1
from itertools import count


class TagCloud:
    def __init__(self):
        self.__tags = {}  # initialize tags attribute to an empty dictionary


    def add(self, tag):
        # first I have to check if I have the tag in the dictionary:
            # if we have it, we'll increment its value by 1
            # if we don't have it, we're gonna set its value to 1
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1  # setting the value for the key
        # we use the get method to get an item by its key and supply a default value if we don't have that

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
        # it means if that key exists it will return its value, if the key doesn't exist it will return 0

    def __setitem__(self, tag, count):  # here tag is my key and count is value of the key, it takes 3 parameters
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags) # iter funct takes an iterable object and returns an iterator object which gives us one item at a time



cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
# What if I add a python tag with capital P i.e. 'Python'
cloud.add("Python")  # I get --> {'python': 3, 'Python': 1} this is how a typical dict behaves
# therefore whatever tag I receive --> def add(self, tag)
# I am gonna convert it to lowercase when setting it i.e. self.tags[tag.lower()]
# as well as when reading it i.e. self.tags.get(tag.lower(), 0) + 1
# print(cloud.__tags)
#  print(cloud["python"]) <-- this will throw an error, because cloud is an object
#if it was a dictionary then you can access value like that, to do this you need to implement a magic method called getitem
print(cloud["python"])
#  cloud["python"] = 2  <-- similarly to set like this, we need to implement magic method called setitem
cloud["python"] = 11
# print(cloud.__tags)
# len(cloud)  <-- to do this, implement len magic method
# print(len(cloud))

# to iterate over cloud using for loop, implement magic method iter
# for tag in cloud:
#     print(tag)


# Think of an iterable like a box that contains toys.
# cloud is the iterable (box).
# An iterator is like a process where you take one toy out of the box at a time.


# PRIVATE MEMBERS

# If I access the underlying dict in this class, run both this code below
# print(cloud.__tags["python"])
# print(cloud.__tags["Python"]) # <--we will get an exception here, because we don't have this key in our dict,
#                            everything is stored as lower case
# So the problem with this class is that it gives access to the underlying dict
# to fix this problem we need to hide this attribute from outside
# to make the attribute private or inaccessible from outside, prefix it with 2 underscore
# i.e.       def __init__(self):
#               self.__tags = {}
# print(cloud.tags) # <- we will get: AttributeError: 'TagCloud' object has no attribute '__tags'
# This is how we can make certain attributes or certain methods in the class private
# If we prefix them with double underscore they are considered private
# Technically they are still accessible, but they are just harder to access now
# Every object has this property called __dict__  <-- this is a dict that holds all the attributes in this class
print(cloud.__dict__)
# output : {'_TagCloud__tags': {'python': 11}}
# when python interpreter runs this code it automatically renames this attribute and prefixes it with name of its class
print(cloud._TagCloud__tags)
# in python, we don't have the concept of private members, this private members are still accessible from outside
# Using double underscore is more of a convention to prevent accidental access of this private members
