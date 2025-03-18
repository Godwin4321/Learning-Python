# In the example below our Animal class has the constructor where we initialize the age attribute to 1
# class Animal:
#     def __init__(self):
#         self.age = 1
#
#     def eat(self):
#         print("Eat")
#
#
# class Mammal(Animal):
#     def walk(self):
#         print("Walk")
#
# m = Mammal()
# print(m.age)



# Now look at this example:
# class Animal:
#     def __init__(self):
#         self.age = 1
#
#     def eat(self):
#         print("Eat")
#
#
# class Mammal(Animal):
#     def __init__(self):
#         self.weight = 2
#
#     def walk(self):
#         print("Walk")
#
# m = Mammal()
# print(m.age)

# In the second example we got this error: AttributeError: 'Mammal' object has no attribute 'age'
# The reason this happened was because the constructor in the Animal class was not executed
# In other words, the constructor that we defined in the Mammal class replaced the constructor in the base class
# This is called "method overriding"
# i.e. we are overriding or replacing a method in the base class
# In the constructor of the Mammal class, we use the built-in super() funct to get access to super or base class

class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()  # calls the parent class's constructor

    def walk(self):
        print("Walk")

m = Mammal()
print(m.age)
print(m.weight)

# super() <-will give access to super/base class, after the dot you can specify any parent class method you want to call.

# method overriding means replacing or extending a method defined in the base class
# In the above code, we're extending the init method that we've defined in the animal class
# If we don't have the line --> super().__init__() in the Mammal class
# the implementation:  def __init__(self):
#                        print("Mammal Constructor")
#                        self.weight = 2
# would completely replace the init method in the animal class



