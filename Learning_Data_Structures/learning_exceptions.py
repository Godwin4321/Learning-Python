# Exception is a kind of error that terminates the execution of a program
# age = int(input("Enter your age: "))
# print(age)
# so I ran the above code, instead of an int I entered s, this is the exception I got for that:
# ValueError: invalid literal for int() with base 10: 's'
# so here, ValueError is the name of the exception
# we can handle this with the help of try and except block
# if code in the try block throws an exception, code in the except block will be executed
# if we don't have an exception, except block will not be executed.
# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("You didn't enter a valid age.")

# we also have an optional else block
# Else block will only be executed if we don't have any exceptions in our try block.
# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")

# When handling the exception in except block
# we can optionally define a variable that will include the details about the exception.
# the name of variable is our choice

# try:
#     age = int(input("Enter your age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown")

# the above code only handles ValueError exception
# what if we have other exception

# try:
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("Age cannot be zero")
# else:
#     print("No exceptions were thrown")


# if any of the statements in the try block throws an exception that matches one of the except block
# that except block is executed and the other except blocks are ignored.


# try:
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):       # handling multiple exceptions
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")


# There are time when we need to work with external resources like files, network connections, databases and so on
# Whenever we use these resources we need to release them after we're done.
# For eg: when we open a file we should always close it after we're done.
# Otherwise an other process or an other program may not be able to open that file

# try:
#     file = open("learning_exceptions.py")  # opening the current python file, open function returns a file object
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):       # handling multiple exceptions
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()

# finally block is always executed whether we have an exception or not
# we use this block to release external resources like files, database connections, or network requests.

# with open("learning_exceptions.py") as file:
# here with file object we can access the return value of open function, just like file = open("file.txt")

# try:
#     with open("learning_exceptions.py") as file:
#         print("File opened.")  #whenever we open a file using the 'with' statement, python will automatically call file.close()
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):       # handling multiple exceptions
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")

# with statement is used to automatically release external resources. we don't need a finally block
# we have methods for our file object
# there are methods which start with two underscore and we refer to them as magic methods
# file.__enter and file.__exit
# when an object has these two methods we say that object supports context management protocol
# so if an object supports context management protocol we can use that object with the 'with' statement
# python will automatically call the exit method there it will release external resources
# That is why we don't need a finally block here


# Raising Exception

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less.")
#     return 10 / age
#
# try:
#     calculate_xfactor(0)
# except ValueError as error:  # error is the name of my exception object
#     print(error)


# Cost of raising exceptions
# If you're building a small application for few users raising exception in your function will not have a bad impact
# on the performance of your application
# But if you're building an application where performance and scalability is important then it's better to raise
# exceptions if you really have to
# As a general rule of thumb, when you want to raise exceptions in your function think twice.

# importing a function called timeit from timeit module
# we can calculate execution time of python code with timeit function.
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age

try:
    calculate_xfactor(0)
except ValueError as error:  # error is the name of my exception object
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None 
    return 10 / age


xfactor = calculate_xfactor(0)
if xfactor == None:
    pass
"""
print("First code: ", timeit(code1, number=10000)) # number=10000, it indicates the number of time we want to execute this code
# the above function i.e.timeit returns execution time of the code

print("Second code: ", timeit(code2, number=10000))

# pass <-- 'pass' statement doesn't do anything, since except block cannot be empty
# None object represents absence of value


