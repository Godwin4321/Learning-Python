# x = 10
# y = 11
# # print(f"Initially, x : {x}, y : {y}")
# # # Swap the above two variables
# # z = x
# # x = y
# # y = z
# # print(f"After swapping, x : {x}, y : {y}")
#
# # we can do the above thing in just one line in python
# x, y = y, x
# print("x", x)
# print("y", y)



# Array
# if you are dealing with a large sequence of number, array is more efficient
# arrays take less memory and perform a little bit faster
# you will see the difference only if you are dealing with a large list of numbers, lets say 10 thousand or more.

# from array import array # importing a class called array from array module
#
# numbers = array("i", [1, 2, 3])   # typecode <- a string which determines the type of our objects
# # "i" means integer i.e. our array is of integer type
# print(numbers.pop())   # we have all the methods exactly like list
# print(numbers)


# Set
# numbers = [1, 2, 3, 2, 4]
# # to remove the duplicates in the above list, we can use set:
# unique_numbers = set(numbers)
# print(unique_numbers)


#Dictionary
# point = {"x": 1, "y": 2}
# print(point)
#another way of defining a dictionary
# point = dict(x=1, y=2)  # dict function takes keyword arguments
# # print(point)
#
# point["x"] = 10  # modifying the dictionary
# point["z"] = 20
# print(point)

# print(point.get("x"))   # will return the value of the key if the key exists, if key doesn't exist it will return None.
# # if you want to show something else if the key doesn't exist then you can do the following:
# print(point.get("k", "key doesn't exist"))
# print(point)
# del point["z"]
# print(point)


# point = {'x': 10, 'y': 2, 'z': 20}
# for key in point:
#     print(key, point[key])

# for key, value in point.items():
#     print(key, value)


# values = []
# for x in range(5):
#     values.append(x * 2)
# print(values)

# let's do the same with list comprehension
# values = [x * 2 for x in range(5)]
# print(values)

# let's do comprehension for sets now
# values = {x * 2 for x in range(5)}
# print(values)

# let's do comprehension for dictionary now
# values = {x: x * 2 for x in range(5)}
# print(values)

# Creating a list using list comprehension
# values = [x * 2 for x in range(10)]
# print(values)
# There will be situations where you will be working with large data sets or perhaps an infinite stream of data
# In those situations u shouldn't store all those values in the memory, because that's very memory inefficient.
# In situations like this it is more efficient to use a Generator object.
# Generator objects are iterable and in each iteration they generate a new value.
# How to get size of an object ? Ans) from sys module import function called getsizeof

# from sys import getsizeof
# values = (x * 2 for x in range(10))  # here values is not a list, it is a Generator object
# print(getsizeof(values))  #our generator object takes ___bytes of memory (run it and see the size displayed on the terminal)


# Unpacking Operator
# [1, 2, 3] <-- for this list, how to get an output like this --> 1 2 3  (i.e. we don't have square brackets and comma)
# To achieve this we can use the unpacking operator
# Unpacking operator can unpack any iterable
# We can use the unpacking operator to take out individual items in any iterable
# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers) #unpacking list
# # Unpacking a string and storing it in list
# char = [*"Hello"]
# print(char)
numbers = [*range(5)]
print(numbers)
# While unpacking dictionaries we need to use two asterisk i.e. **





