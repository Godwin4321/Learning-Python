# We use for loops to iterate over iterable objects
# we use for loops to iterate over all the items in a collection.

#for item in "Python":  # item is the loop variable
 #   print(item)

#in first iteration, 'item' variable will hold the value 'P' then 'y' and so on.


#prices = [10, 20, 30,]
#sum_of_price= 0
#for price in prices:
 #   sum_of_price += price
#print(f"Sum of all the prices: {sum_of_price}")


# Nested loops -> i.e. one loop inside another loop

#for x in range(0, 3):
 #   for y in range(0, 2):
  #      print(f"({x})({y})")

'''
numbers = [2, 2, 2, 2, 10]

for star_count in numbers:
    pattern = ""
    for count in range(star_count):
        pattern = pattern + "*"
    print(pattern)
'''

'''
#Learning the range function
for number in range(1, 4):
    print("Attempt", number)
'''

'''
# range function one level up
for number in range(1, 11, 3):
    print("Attempt", number, "*" * number)
'''

'''
# for...else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times but failed")
'''

#even numbers from 1 to 10
even_number = 0
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
        even_number += 1
print(f"We have {even_number} even numbers.")