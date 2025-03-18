# class Mammal:
#     def eat(self):
#         print("Eat")
#
#     def walk(self):
#         print("Walk")
#
#
# class Fish:
#     def eat(self):
#         print("Eat")
#
#     def swim(self):
#         print("Swim")


# As you can see we have repeated or duplicated the eat method in both the classes
# In programming we have a concept called DRY --> Don't Repeat Yourself
# To solve this problem we have 2 solutions 1) Inheritance or 2) Composition
# let's look at inheritance
# Inheritance is a mechanism that allows us to define the common behaviour or common functions in one
# class, and then inherit them in other classes


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")

# Animal: Parent class or base class
# Mammal, Fish: Child class or subclass

class Mammal(Animal): # Mammal class inherits all the features of the Animal class
    def walk(self):
        print("Walk")

class Fish(Animal):    # Fish class inherits all the features of the Animal class
    def swim(self):
        print("Swim")

m = Mammal() # creating a mammal object
m.eat()
print(m.age)




