# class InvalidOperationError(Exception):
#     pass
#
# class Stream:
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open.")
#         self.opened = True
#
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False
#
# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")
#
# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# There are a couple of issues with the above implementation.
# First issue is that we can create an instance of Stream class and call the open method
# stream = Stream()
# stream.open()
# What does it mean to open a stream ? are we working with a file stream here, a network stream, what kind of stream ?
# So we shouldn't be able to directly create an instance of the Stream class, we should always subclass it and then create an
# instance of the subclass, this is the first issue
# Second issue: If you look at the implementation of the FileStream, NetworkStream classes, both these classes have a read method
# If tomorrow we decide to create a different kind of stream we should remember to implement the read method, call it exactly read
# if we call it readline, or readstr or read something, it's not gonna be consistent
# It will be nice to have a common interface across these different types of stream, so how can we solve these problems ?
# That's when we use Abstract Base class
# Its purpose is to provide some common code to it's derivatives
# so here we wanna make Stream class an abstract base class.
# to do that: from abc module we import the ABC class and abstractmethod funct which we're going to use as a decorator
# abc -> abstract base class,    name of the module -> all lower case,   name of the class -> all upper case

# step 1: to make Stream class abstract, we should derive it from ABC class
# step 2: to define the common interface for all streams
#         we want all streams to have read method
# When a class has an abstract method, its considered an abstract class and we cannot instantiate them

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):    # to make Stream class abstract, we should derive it from ABC class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

memorystream = MemoryStream()
memorystream.open()

# If a class derives from the Stream class it has to implement the abstract method here it is read otherwise that class will also
# be considered abstract
# so if i create a new class, eg: class MemoryStream(Stream):
#                                       pass
# so above our new class MemoryStream is also abstract, if we wanna make it a concrete class so we can instantiate it, we will
# have to implement the read method
# Therefore, class MemoryStream(Stream):
#                   def read(self):
#                          print("Reading data from a memory stream")

# Now the MemoryStream is a concrete class, we can instantiate it
# Now all our streams have read method




















