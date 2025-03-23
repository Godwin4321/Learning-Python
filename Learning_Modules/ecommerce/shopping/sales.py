# print("Sales initialized", __name__)  # __name__  <-- will return the name of the module
# if we run this file output: Sales initialized __main__
# the name of our module is changed to __main__
# so the name of the module that starts our program is always __main__


def calc_tax():
    pass

def calc_shipping():
    pass

if __name__ == "__main__":
    print("Sales started")
    calc_tax()
# With the above 3 lines of code we can make this file usable as a script as well as a reusable module
# that we can import into another module
# so if we run this file directly, the name of this module will be __main__ and inside the if statement
# we can have any initialization code, or we can call one of the existing functions in this module
# However if we import this module into another module code inside the if statement will not be executed
# because at that point the name of this module will no longer be __main__  it will be
# ecommerce.shopping.sales




# Here in our sales module currently we've defined 2 functions, but we can also write any statements
# and these statements will be executed the first time this module is loaded.
# So if we import this module and there are few different modules in our program, python will only
# load this module once and then cache it in memory, so the statements that we write here will be executed
# once


# Now let's suppose I want to use the contact module in customer package here
# To import a module from another package we can use an absolute or relative import statement

# Absolute import:
# our top level package is Learning_Modules
# from Learning_Modules.ecommerce.customer import contact  # <- Absolute import
# contact.contact_customer()

# Relative import:
# from ..customer import contact  # <- importing the contact module
#    .  <-  represents the current package
#   ..  <-  takes us one level up
# contact.contact_customer()

# As a best practice prefer to use Absolute import but if your absolute import gets really verbose
# like a.b.c.d.e then simplify the import statement using relative import
# verbose means using more words than necessary or being overly detailed.
