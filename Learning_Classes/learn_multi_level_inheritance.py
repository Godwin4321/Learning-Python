class Animal:
    def eat(self):
        print("Eat")

class Bird(Animal):
    def fly(self):
        print("Fly")

class Chicken(Bird):
    pass   # using pass statement to define an empty class

# pass is a statement that doesn't do anything, we just use it to make python interpreter happy, because
# we cannot have a class without anything in it.
# Too much inheritance between classes can increase complexity and introduce various kinds of issues.
# The above code is an example of inheritance abuse, because Chicken class inherits all features of Bird
# class, but chicken cannot fly :)
# Employee - Person - LivingCreature - Thing
# This is multi-level inheritance, which can significantly increase the complexity of software.
# If you want to use inheritance limit it to one or two levels.