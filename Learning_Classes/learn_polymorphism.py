# from abc import ABC, abstractmethod
#
# class UIControl(ABC): #defined an abstract base class called UIControl
#     @abstractmethod
#     def draw(self): # this method has no implementation
#         pass
#
# # Now we have 2 classes that derive from UIControl class
#
# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")
#
# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")
#
# # A funct called draw that takes a UIControl object and calls the draw method on it
# def draw(control):
#     control.draw()
#
# # perfectly fine because ddl is an instance of the UIControl class, let's verify
# # print(isinstance(ddl, UIControl))
# # i.e. DropDownList object is an instance of UIControl class and that means wherever we expect a UIControl object we can
# # pass any of its derivatives like a TextBox object or DropDownList object
#
# ddl = DropDownList()
# draw(ddl)
# textbox = TextBox()
# draw(textbox)


# Let's change the draw funct, so instead of getting a control object let's get a list of controls
from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()  # calling the draw method on each control object

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])  # passing a list of 2 objects

# So using this approach we can render the user interface of an application.
# Imagine we have a form with a bunch of textboxes, drop-down lists, radio-buttons and so on
# We could have a list of all these objects and pass that list to a function like draw and that function will take care
# of rendering the entire form
# "Poly" means Many, "morp" means Forms i.e. Polymorphism means Many Forms
# In this example our draw method has taken many different forms and this is determined at runtime
# we could be calling the draw method on textbox, or a dropdownlist, radiobutton, so on
# Polymorphism allows different objects to use the same method but behave differently based on the object calling it.


