# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.
import random

userNumbers = []

for i in range(0, 6):
    userNumbers.append(int(input("Podaj " + str(i + 1) + ". liczbę od 1 do 49: ")))

numbers = [i for i in range(1, 49 + 1)]
randomNumbers = random.sample(numbers, 6)
print("Wylosowane liczby to:", randomNumbers)

counter = 0
for i in range(0, 6):
    if userNumbers[i] in randomNumbers[:]:
        counter += 1

print("Udało Ci się zgadnąc " + str(counter) + " liczb.")
