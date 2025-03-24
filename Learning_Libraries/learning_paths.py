# Let's learn about the Path class, which is the foundation to work with files and directories
# from pathlib module let's import the Path class
from pathlib import Path
# now we can create Path object in a few different ways
# we can create an absolute path
# Path("C:\\Program Files\\Microsoft")
# this double backslashes get ugly, so we can simplify this by using a raw string
# In a raw string backslash is not an escape character i.e. Path(r"C:\Program Files\Microsoft")

# Creating an absolute path on linux :
# Path("/home/avager/Desktop")  # i.e. giving the full path

# Creating a Path object that represents the current folder
# Path()

# Using a relative path
# Path("Learning_Libraries/learning_paths.py")
# Learning_Libraries  <- current folder

# We can also combine Path objects together
# Path() / Path("Learning_Libraries")

# We can also combine a Path object with a string
# Path() / "Learning_Libraries" / "learning_paths.py"

# We can also get the home directory of the current user
# Path.home()  # home() method which returns the home dir of the current user

# These are various ways to create a Path object

path = Path("/home/avager/PycharmProjects/PythonProject/HelloWorld/Learning_Libraries/learning_paths.py")
print(path.exists()) # <- to see if this file or dir exists or not

# to check to see if this path represents a file
print(path.is_file())
# we also have path.is_dir()

# We can also extract individual components in this path, which is extremely useful
print(path.name)  #output: learning_paths.py
print(path.stem)  #output: learning_paths
print(path.suffix)  #output: .py

# to get parent of this path
print(path.parent)  #output: /home/avager/PycharmProjects/PythonProject/HelloWorld/Learning_Libraries

# we can use this to create a new path object based on the existing path but only change the name and
# extension of the file
path = path.with_name("file.txt") # <- we get a new path object here
print(path) #output: /home/avager/PycharmProjects/PythonProject/HelloWorld/Learning_Libraries/file.txt
# file.txt doesn't exist, they are only representing its path

# Similar to this with_name we have another method with_suffix() and we use that to change the extension
# of the file
path = path.with_suffix(".py")
print(path) #output: /home/avager/PycharmProjects/PythonProject/HelloWorld/Learning_Libraries/file.py
# Note that here we've not renamed the file, we're only representing a Path object



# If you want to refer to the folder you are currently in, simply use:
path = Path(".")
print(path.exists())  # This will return True

# #Or, if you want to reference the file within the current directory, you could use its name directly:
# file_path = Path("learning_paths.py")
# print(file_path.exists())  # This should return True










