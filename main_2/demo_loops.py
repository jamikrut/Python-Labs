# wyświetl wszystkie cyfry

i = 0
while i < 10:
    print(i, end=" ")
    i += 1

print("\n")

for i in range(0, 10):  # i < 10
    print(i, end=" ")

print("\n")

for i in range(10):  # to same co range (0, 10, 1)
    print(i, end=" ")

print("\n")

# początek i = 2
# dopóki dopóki i < 10
# skaczem co 3 (i += 3)
for i in range(2, 10, 3):
    print(i, end=" ")

print("\n")

for i in range(9, 1, -1):
    print(i, end=" ")

print("\n")

# 3! = 1 * 2 * 3 = 6
number = 13
factorial = 1

for i in range(1, number + 1):
    factorial *= i
print(factorial)
