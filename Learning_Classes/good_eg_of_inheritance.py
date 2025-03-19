# Stream is a way of handling data
# Analogy: Water Pipe
# The water flowing inside the pipe is data.  The pipe itself is the stream that transports the water.

# Let's imagine we wanna model the concept of a stream of data
# We can read a stream of data from a file, from a network, or from the memory.
# All these streams have a few things in common, we can open them, we can close them, we can read data from them
# But how we read data from a stream is dependent upon the type of the stream
# For example reading data from a file is different from reading it from a network
# Let's define a base class called Stream.

class InvalidOperationError(Exception):  # deriving it from the base Exception class
    pass

class Stream:
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

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

# Stream class contains all common features that we need in every stream
# Base class: Stream
# subclasses:   FileStream
#               NetworkStream

# open method logic
# here let's create a flag to know if the stream is open or not.
# setting opened initially to False in the constructor
# What if we try to open a stream that is already opened, invalid operation therefore raise an exception

# creating a custom exception logic
# by convention all custom exceptions should end with Error i.e. InvalidOperation"Error"
# everytime you wanna create a custom exception you should derive your class from the Exception class