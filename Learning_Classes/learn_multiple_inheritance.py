# In python a class can have multiple base classes
# So here, we have a Manager class with two base classes.
# This is called multiple inheritance.
# Similar to multi-level inheritance if you don't use it properly you will get many bugs.

class Employee:
    def greet(self):
        print("Employee greet")

class Person:
    def greet(self):
        print("Person greet")

class Manager(Employee, Person):
    pass

# Let's see what happens when we create a manager object and call the greet method
# Which greet method will be called ?

manager = Manager()
manager.greet()
# First it looks at the Manager class to see if it has a method called greet in it.
# There is no method called greet in Manager class, therefore now it will look at base class.
# Since we added Employee class first i.e. (Employee, Person) therefore we will get greet method of Employee class


# Multiple inheritance is not always a bad thing, it's bad if you don't use it properly.
# if the classes have nothing in common, and you want to inherit their features in a separate class that is perfectly
# fine to use multiple inheritance.
# Things start to get complicated when these classes have things in common like the greet method here.
