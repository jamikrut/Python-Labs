numbers = [4, 5, 2, 1, 3, 10, 12, 99, 87, 32, 105, 101, 8, -2]
swapped = True  # czy jest posortowana

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True


print(numbers)

'''
for i in range(1, len(numbers)):
    if numbers[i - 1] > numbers[i]:
        numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
'''

numbers = [4, 5, 2, 1, 3, 10, 12, 99, 87, 32, 105, 101, 8, -2]
numbers.sort(reverse=True)

print(numbers)
