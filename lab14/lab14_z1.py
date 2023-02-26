# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.

phone_numbers = {"Agata": 234356874,
                 "Beata": 567346865,
                 "Aleksandra": 843946429,
                 "Zuzanna": 738928348
                 }

name = input("Podaj imię: ")
if phone_numbers.get(name) == None:
    print("Nie ma takiej osoby w książce!")
else:
    print("Numer telefonu:", phone_numbers.get(name))
