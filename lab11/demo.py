a = 1
b = 4
print("a =", a, "b =", b)

a, b = b, a
print("a =", a, "b =", b)

numbers = [1, 2, 3]
numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)

letters = ["A", "C", "", "B"]
print(letters)
print(ord("A"), ord("C"), ord("a"))

letters.sort()
print(letters)

'''
list_1 = [9]
list_2 = list_1
list_2[0] = 13
print(list_2)
print(list_1)
'''

list_1 = [9]
list_2 = list_1[:]  # kopia całej listy
list_2[0] = 13
print(list_2)
print(list_1)

# uwuwanie wycinków list
del numbers[1:3]
# del numbers[:] -> wszytskie elementy
del numbers # cała lista
