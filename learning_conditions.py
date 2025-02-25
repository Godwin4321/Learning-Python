'''
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a lovely day")

print("Enjoy your day :) ")
'''

'''
good_credit = False

if good_credit:
    print("Put down 10%")
else:
    print("Put down 20%")
'''


'''
#Logical Operators
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
'''

'''
#Comparison operators
temperature = 15

if temperature >= 30:
    print("It's a hot day")
elif temperature <= 10:
    print("It's a cold day")
else:
    print("It's a lovely day")

print("Enjoy your day :) ")
'''

name = input("Enter your name: ")
name_length = len(name)
#print(name_length)

if name_length < 3:
    print("Name must be at least 3 characters")
elif name_length > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")