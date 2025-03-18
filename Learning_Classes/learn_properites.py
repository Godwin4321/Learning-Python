# class Product:
#     def __init__(self, price):
#         self.set_price(price)  # setting value for the attribute
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value
#
#
# product = Product(-50)
from itertools import product


# The above code is unpythonic, means it is not using python's best practices
# not using the language to its fullest potential
# To achieve the same result we have a better way
# That's when we use a property
# A property is an object that sit in front of an attribute and allows us to get or set the value of an attribute


# class Product:
#     def __init__(self, price):
#         self.set_price(price)  # setting value for the attribute
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value
#
#     price = property(get_price, set_price)  # passing reference to the funct not calling them
#     #property funct will return a property object that property object will use get_price funct for reading the value of
#     # the price attribute
#     #property funct takes 4 parameters and all these parameters are optional
#         # 1st para = func for getting value of the attribute
#         # 2nd para = func for setting the value of the attribute
#         # 3rd para = funct for deleting that attribute
#         # 4th para = documentation
#
# product = Product(10)
# print(product.price)  # product object with price property
# product.price = 20   # we can also set it
# print(product.price)
# So a property looks like a regular attribute from outside but, internally it has two methods 1)getter & 2)setter

# We want our objects and classes with minimal number of functions or methods exposed to outside
# We can do this by prefixing with double underscores but, there is a better, shorter & cleaner way to achieve the same
# result
# We can use a decorator
# Earlier we used a decorator called @classmethod to convert an instance method to a class method
# We have another decorator for creating a property, so instead of explicitly calling the property funct to create a
# property object, we can apply the @property decorator

class Product:
    def __init__(self, price):
        self.price = price # using price property as a regular attribute

    @property      # applying property decorator to this method, when python interpreter see's this code it will
    def price(self):  # automatically create a property object called price
        return self.__price

    @price.setter      #here price is the name of the property
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

product = Product(-10)


# When defining properties, you don't always have to define a getter and a setter
# if we comment out @price.setter, we will have a read only property