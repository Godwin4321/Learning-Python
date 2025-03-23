# Imagine going to a supermarket with all products in one section, finding a product there is really hard
# That's why we have various departments/sections in a supermarket.
# We have the same concept in programming
# As our program grows, we should split our code across multiple files, we refer to each file as a module.
# i.e. module is a file which contains some python code.
# In a supermarket each section contains highly related products, only fruits in fruits section, similarly a
# module should contain highly related objects, these objects can be functions, classes, variables, and so on.
# In terms of naming convention just like variables and functions we use all lower case letters and if we have
# multiple words we separate them using an underscore.

# from sales import calc_shipping
# # to import multiple objects from a module, we separate them using a comma
# from sales import calc_shipping, calc_tax

# from sales import *   <-- bad practice, because in that module we could have several different functions
# or variables and if you blindly import them into the current module some of them may override the objects
# with the same name in the current module, so don't import all objects like this.

#
# calc_shipping()  # calling that function
# calc_tax()

# Another way to import a module
# import sales
# now in this module we have an object called "sales", and we can use the dot operator to access its members
# sales.calc_shipping() # now calc_shipping() funct is now a method in this object.


# So basically we can either import the entire module as an object i.e. import sales
# or we can import specific objects from that module i.e. from sales import calc_shipping



# Compiled Python Files

# When I run this program you will see a new folder in our current folder called __pycache__
# In this folder __pycache__, we have the compiled version of the modules that we import into our program
# So we will have a compiled version of the sales module
# The reason python stores the compiled version in the folder __pycache__ is to speed up module loading
# So next time we run our program python will look at the content of the folder and if we have the compiled
# version of the imported module python will simply load that compiled version, so it will skip that compilation
# step and this will result in the faster loading of the sales module.
# sales.cpython-312.pyc  <-- cpython-312 represents the python implementation used to compile this file
# so we have compiled this file using cpython version 3.12
# in the file i.e. sales.cpython-312.pyc, we have python byte code



# Module Search Path

# import sales
# When python sees this it will look for a file called sales.py in the current directory
# If it doesn't find this file it will look in a bunch of predefined directories that come with python
# installation
# import sys  # built-in module
# in this module we have a variable called path, which returns the list of directories that python will look at
# to find a module.
# print(sys.path)
# the first element in this list represents the current folder
# so when python sees an import statement it will search all these directories to find the module, as soon as it
# finds the module the search stops there.




# Python packages

# moving the sales module to a directory called ecommerce which is subdirectory of Learning_Modules

# import sales  # <- error because python cannot find sales module
# To fix this issue go back to the ecommerce folder and create a new file called __init__.py
# When we add this file, python will treat the ecommerce folder as a package
# So a package is a container for one or more modules
# in file system terms, a package is mapped to a directory and a module is mapped to a file.
# Now prefix the name of the module with the name of its package
# import ecommerce.sales
# now to use any of the objects in the sales module we need to prefix them with the name of the package and
# modules
# ecommerce.sales.calc_tax()
# This way we will have to type a lot which is tedious
# Better approach:
# from ecommerce import sales
# importing the sales module as an object then we can use the dot operator to access all the members of module.
# sales.calc_shipping()


# Sub-packages
# Let's create a new folder insider ecommerce folder called shopping
# Now lets move our sales module into our shopping folder.
# Now don't forget to create a file called __init__.py inside the shopping folder
# After adding this file python will treat shopping folder as a package
# Now add the name of the sub-package
# from ecommerce.shopping import sales



# The dir() function
# from ecommerce.shopping import sales # importing sales module

# dir() function returns list of attributes and methods defined in an object

# Sometimes things don't work as you expect so you can use the dir function for debugging

# print(dir(sales))
# output:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#              '__package__', '__spec__', 'calc_shipping', 'calc_tax', 'contact']
# as you can see in the list we have some magic attributes which are automatically created for us
# and also our functions calc_shipping and calc_tax which we defined.

# print(sales.__name__)  # returns the name of our module
# print(sales.__package__) # returns the name of our package

from ecommerce.shopping import sales
# using the same technique we can write the initialization code for our packages






