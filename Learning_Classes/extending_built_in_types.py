# In python, we can also use inheritance with the built-in types.

class Text(str):     # class Text inherits from built-in String class
    # our Text class will inherit all the feature of python string, and we can also add additional features
    def duplicate(self):
        return self + self    # self represents the current object, here we're concatenating a string with itself

text = Text("Python")
print(text.lower())  # method of class string
print(text.duplicate())  # method of class Text

class TrackableList(list): # class TrackableList inherits from built-in list class

    def append(self, object): # extending the append method of the built-in list class but not replacing it
        print("Append Called")
        super().append(object) # calling the append method of the base class

list = TrackableList()
list.append("1")
list.append("1")

# Summary:
# When you create a TrackableList object and append "1", it prints "Append Called" and then adds "1" to the list.
print(list)