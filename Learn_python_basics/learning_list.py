#names = ["John", "Mona", "Lisa", "Tom", "Jerry"]
#names[0] = "Jon"
#print(names)

#Program to find a largest number in a list.
'''
numbers = [2, 12, 6, 7, 20]
max = numbers[0] # Assuming first number of the list is the largest.

for number in numbers:
    if number > max:
        max = number  # resetting max to the new number

print(max)
'''

# 2D Lists

matrix = [
    [1, 2, 3],            #Here matrix is a 2D List
    [4, 5, 6],            # Each item of the matrix list is another list
    [7, 8, 9]             # Here matrix has 3 lists inside it
]
print(len(matrix))
print(matrix[0])
print(matrix[0][0])
print("-----------------------")

#matrix[0][0] = 20
#print(matrix)

for row in matrix:
    for item in row:
        print(item)





