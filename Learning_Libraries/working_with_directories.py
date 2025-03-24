# first let's change the configuration of this script by going to configuration and setting the
# working directory as /home/avager/PycharmProjects/PythonProject/HelloWorld

from pathlib import Path

path = Path("Learning_Libraries")
# print(path.exists())
# path.mkdir()  # <- to create a new directory
# path.rmdir()  # <- to remove a directory
# path.rename()  # <- to rename it to a new name

# print(path.iterdir())  # output: generator object
# with this method we can get the list of files and directories in the path we mention

# a generator object as the name implies returns a new value everytime we iterate it
# so when we're working with a large list of items instead of storing all those items in the memory we
# use a generator object, we iterate it and get a new value everytime, this is more efficient.
# When working with files and directories it is possible that we can have a directory with a million
# files in it.

# for p in path.iterdir():
#     print(p)
# output: Learning_Libraries/working_with_directories.py
#         Learning_Libraries/learning_paths.py
# So I have 2 files in this path

# If you're working with a directory that doesn't have a million files in it, you can convert this
# generator to a list using a list comprehension expression
# instead of iterating over this generator, let's use a list comprehension
# paths = [p for p in path.iterdir()]  # for p in path.iterdir(), p will be returned
# print(paths)
# output: [PosixPath('Learning_Libraries/working_with_directories.py'),
#                    PosixPath('Learning_Libraries/learning_paths.py')]
# We get a list of PosixPath objects
# The Path class that we imported on the top is the base class for 2 different classes
# PosixPath and WindowsPath, Posix is the standard used in Unix like operating system

# taking the comprehension expression to the next level
# lets only get the directories
# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)
# I got an empty list because there are no directories inside my Learning_Libraries directory

# therefore iterdir() method is very useful to get the list of files and directories in a path
# But it has 2 limitations : 1) we cannot search by a pattern
#                            2) it doesn't search recursively
# so for those scenarios we need to use a different method called glob()
# path.glob() #this method takes a pattern
#   *.*   <-- search for all files
#   *.py  <-- search all .py files
# similar to other method this returns a generator
# therefore we can use an expression
# py_files = [p for p in path.glob("*.py")]
# print(py_files)
#output: [PosixPath('Learning_Libraries/working_with_directories.py'),
#                   PosixPath('Learning_Libraries/learning_paths.py')]
# So in my directory Learning_Libraries, I have 2 py files.


# to search recursively, rglob -> recursive glob
py_files = [p for p in path.rglob("*.py")]
# we will get all the py files in the current directory and all its children
# means if there are any py files inside the subdirectory of the current directory it will also list that
print(py_files)









