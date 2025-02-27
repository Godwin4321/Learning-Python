'''
if age >= 18:
    message = "You're eligible"
else:
    message = "You're not eligible"
print(message)
'''

#Ternary operator
'''
age = int(input("Enter your age: "))
message = "You're eligible" if age >= 18 else "Not eligible"
print(message)
'''

#Chaining comparison operator
'''
age = 21
if 15 <= age <= 35:
    print("Age is just a number")
'''

high_income = False
good_credit = True
student = True

message = "You're eligible" if (high_income or good_credit) and student else "Not eligible"
print(message)
