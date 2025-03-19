# from abc import ABC, abstractmethod
#
# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")
#
# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")
#
#
# def draw(controls):
#     for control in controls:
#         control.draw()  # calling the draw method on each control object
#
# ddl = DropDownList()
# textbox = TextBox()
# draw([ddl, textbox])

# So to define a polymorphic behaviour we start by defining a base class and in that class we define the common behaviour or the
# common methods that we need in its derivatives or children.
# on line 20 we achieve polymorphic behaviour
# so depending on the type of control object that we're working with at runtime, draw method takes a different form
# it might be the draw method at the textbox, or dropdown list, and so on
# Since python is a dynamically typed language, we don't necessarily need the base class i.e. UIControl as the base class i.e.

class TextBox:
    def draw(self):
        print("TextBox")

class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()  # calling the draw method on each control object

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

# With this change we can still achieve polymorphic behaviour
# controls parameter in draw funct, we haven't specified the type of that parameter, it is purely a label
# we can pass any kind of objects to this draw function, as long as that object is iterable python will be happy
# since on line 43 we're looping over that object, so that object has to be iterable
# so technically we can pass a string, a list, a tuple, a dictionary, anything that is iterable
# That iterable object, its individual part should have a draw method, as long as these objects have draw method python will be
# happy. This is what we call Duck Typing, if it walks like a duck and quacks like a duck it is a duck
# since python is a dynamically typed language, it doesn't check the type of object, it only looks for the existence
# so on line 44 it only looks for the existence of the draw method
# To achieve polymorphic behaviour we don't necessarily need a base class like UIControl because python supports duck typing
# Having said that, having that UIControl as an abstract base class is a good practice because it enforces a common interface
# across all its derivatives, with this we will make sure every kind of UIControl will have a draw method












