numbers = [1, 2, 3]
matrix = [numbers[:], numbers[:]]

numbers[0] = 99

print(numbers)
print(matrix)

matrix[0][0] = 88
print(matrix)
