amount = int(input("Liczba imion w zbiorze: "))
names = []

for i in range(1, amount + 1):
    name = input("Podaj " + str(i) + ". imię: ")
    names.append(name)

print("\nOto lista imion:")
for i in range(1, amount + 1):
    print(str(i), names[i - 1])
