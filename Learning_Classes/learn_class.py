# class Point:
#     def draw(self):
#         print("draw")
#
# # Every point object that we create will have this draw method
#
# # Creating a point object and assigning it to a variable
# point = Point()
# # print(type(point))
#
# # sometimes we wanna know if an object is an instance of a class at such times use isinstance() funt
# print(isinstance(point, Point)) #checking if point object is an instance of Point class
# print(isinstance(point, int)) #checking if point object is an instance of int class



# Let's learn about constructors

# class Point:
#
#     default_color = "red"
#
#     def __init__(self, x, y):
#         self.x = x    # setting value for the attribute
#         self.y = y    # setting value for the attribute
#
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
#
#
# Point.default_color = "blue"
# point = Point(1,2)
# print(point.x)
# point.draw()
#
# another = Point(3,4)
# another.draw()
#
# print(point.default_color)
# print(another.default_color)
# print(Point.default_color)


# Class Methods
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def zero(cls):
#         return cls(0, 0)
#
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
#
# point = Point.zero()
# point.draw()


# Magic Methods
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# # magic methods are called automatically by python interpreter
# point = Point(1, 2)
# print(point)


# Comparing objects
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other) # <- we will get false here, because by default this equality operator "==" compares the references/addresses
                     # of this two objects in memory, therefore we get false because both objects are stored at diff memory location

# We can solve this problem by a magic method, that magic method is called when we compare two objects

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):     # this method requires two parameters
#         return self.x == other.x and self.y == other.y
#
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
#
# point = Point(10, 20)
# other = Point(1, 2)
# print(point < other)  # self always refers to the object on the left side of the operator.
#                       # other refers to the object on the right side of the operator.
#
# # When you implement the greater than magic method python will automatically figure out what to do if I use the less than operator



# Arithmetic operations with magic method

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y) # will return a new point object


point = Point(10, 20)
other = Point(1, 2)
combined = point + other # storing result in another object :)
print(combined.x, combined.y)