# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 3
# # print(zeros)
# combined = zeros + letters # concatenating lists
# # print(combined)
# numbers = list(range(11))  #list function takes iterable objects and converts them into list
# #print(numbers)
#
# chars = list("Hello World") #String is also an iterable object
# print(len(chars))
from operator import index

# Accessing items of a list
# numbers = list(range(20))
# print(numbers[::-1])

#List Unpacking
# numbers = [1, 2, 3]
# first, second, third = numbers  #unpacking items of the list into variables
# print(f"Items of the list are {first}, {second} and {third}")

# suppose if our list has many items
#numbers = [1, 3, 5, 2, 7, 9]
# first, second, *remaining_numbers = numbers #unpacking two items and packing remaining items into a list
# print(first)
# print(second)
# print(remaining_numbers)

# first, *remaining_numbers, last = numbers
# print(first, last)
# print(remaining_numbers)

# Looping over list
# letters = ["a", "b", "c"]
# for letter in enumerate(letters):
#     print(letter[0], letter[1]) #accessing element at index 0 and index 1 of the tuple

# letters = ["a", "b", "c"]
# for index, item in enumerate(letters): # tuple = (0, 'a')
#     print(index, item)                 # index, item = tuple  i.e. unpacking items of the tuple into variable


# letters = ["a", "b", "c", "d"]
# add items to the end of the list
# letters.append("e")
# print(letters)
# insert item at a particular index
# letters.insert(1, "_")
# removing items from the end of the list
# letters.pop() # we can also add index of the item, if we want to remove an item by the index
# pop method removes a single item, to remove a range of item we can use the delete statement
# del letters[0:2]
# print(letters)
# letters.clear()  #to remove all the items(i.e. objects) of the list
# print(letters.index("a")) # to find index of an object in the list

# how to find index of an object which is not present in the list
# print(letters.index("f"))  # <-- it will throw an error, therefore to prevent this we do:
# if "f" in letters:
#     print(letters.index("f"))
# #to find no of occurrences of a given item in the list:
# print(letters.count("a"))


#Sorting lists

# numbers = [3, 51, 2, 8, 6]
# # numbers.sort()
# # print(numbers)
# # numbers.sort(reverse=True)  #to sort numbers in reverse order
# # print(numbers)
# # .sort() modifies the original list
# # print(sorted(numbers)) # new list i.e. sorted
# print(sorted(numbers, reverse=True))  # to reverse the list
# print(numbers)  # the original list


# items = [
#     ("Product1", 10),       # items list has 3 items in it, also the 3 items are tuples.
#     ("Product2", 9),        # each tuple has 2 items in it (number is the price of the product)
#     ("Product3", 12)
# ]
#
# # creating a function to sort items of the list "items"
# # def sort_items(item):
# #     return item[1]
#
# # items.sort(key=sort_items)    # sort function will return each item of the list "items" to sort_items function,
# #                 # sort_items function will return the price of the product back to sort function so that it can sort the list
# # print(items)
#
# # Doing the same with lambda function
# items.sort(key=lambda item: item[1])
# print(items)


# Learning map function
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]
# # prices = []
# # for item in items:
# #     prices.append(item[1])
# # print(prices)
#
# # the above thing can be achieved with the help of map function
# prices = list(map(lambda item: item[1], items))
# print(prices)


# Learning the filter function

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]
#
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


# The zip function

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
#
# # now if we want to combine this 2 list in a way like this:
# # [(1, 10), (2, 20), (3, 30)]
# # if you see our list has 3 items, each item is a tuple
# # (1, 10)  --> here 1 is the first element of the list1, 10 is the first element of list2
# # We can achieve this by :
#
# print(list(zip(list1, list2)))  # zip function takes an iterable object and also returns an iterable object.


# Stacks
# browsing_session = []
#
# # Check if the stack is empty or not
# # [] --> empty stack --> gives False in boolean context
# # if stack is empty print "disable the back button"
# if not browsing_session:
#     print("Stack is empty")
# print("Done")


# Queue
# from collections import deque  # collections <- module, deque <- class
# queue = deque([])   # wrapping our list with dequeue object, now this dequeue object has methods just like our list object
# # queue.append(1)
# # queue.append(2)
# # queue.append(3)
# # print(queue)
# # # to remove an item from the beginning of the queue
# # queue.popleft()
# # print(queue)
# if not queue:
#     print("Queue is empty")


# Tuple
# point = 1,
# print(type(point))
# print(point)

#concatenating tuple
# point = (1, 2) * 2
# print(point)

#converting a list to a tuple
point = tuple([1, 2]) #tuple function takes iterable
print(point)
# accessing items in a tuple is same as like accessing items in a list
