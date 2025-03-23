'''
# Creating my own function
def greet(first_name, last_name):   # defining the function
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")

greet("Godwin", "Jayakumar")  #calling the function
'''

'''
# Creating a function which returns a value
def greet(first_name, last_name):
    return f"Hi {first_name} {last_name}"


print(greet("Godwin", "Jayakumar")) #calling the function
'''

'''
# Using "keyword arguments" to make my code more readable
def increment(number, by):
    return number + by


print(increment(5, by=1)) #used keyword arguments, we can use it when we have multiple arguments in our function
'''

'''
# Default Arguments
def increase(number, by=1): #default value of the parameter
    return number + by


print(increase(5, 2))
'''


# How to provide multiple arguments to a function
# def multiply(*numbers):  #The *numbers parameter allows the function to accept multiple arguments as a tuple.
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
# print("Start")  #for debugging
# print(multiply(2, 3, 4, 5))  # providing multiple arguments


'''
# With '**' we can pass multiple keyword arguments, python automatically packages them into a dictionary.
def save_user(**users):
    #print(users)
    print(users["age"])



save_user(id=1, name="John", age=22)
'''


# Fizz buzz problem

def fizz_buzz(input_number):
    if (input_number % 3 == 0) and (input_number % 5 == 0):
        return "FizzBuzz"
    if input_number % 3 == 0:
        return "Fizz"
    if input_number % 5 == 0:
        return "Buzz"
    return input_number


print(fizz_buzz(7))









