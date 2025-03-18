class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal): # Mammal class inherits all the features of the Animal class
    def walk(self):
        print("Walk")

m = Mammal()
# isinstance()  <-- it tells if an object is an instance of a given class
# print(isinstance(m, Mammal))
# print(isinstance(m, Animal)) # True <- because Mammal inherits from Animal

# An interesting fact
# The Animal class that we defined above inherits from another class called object even though we didn't
# write like this : class Animal(object)

# We have a class called "object" which is the base class for all classes in python.
# So every class we have directly or indirectly derives from the object class
# print(isinstance(m, object))
# so Mammal inherits from Animal which inherits from object

# to see if a class derives from another class
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))





