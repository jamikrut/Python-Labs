print("Te liczby to: ", end="")
counter = 0
for i in range(1, 101):
    if i > 90 and i % 2 == 0:
        print(i, end=" ")
        counter += 1
    elif i % 2 != 0 and i % 9 == 0:
        print(i, end=" ")
        counter += 1
print("\nŁączie jest to " + str(counter) + " cyfr.")
