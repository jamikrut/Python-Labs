# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.


def bodyMassIndex(height, weight):
    return weight / (height / 100) ** 2


def interpreterBMI(BMI):
    if BMI > 40:
        return "otyłość III stopnia"
    elif BMI >= 35:
        return "otyłość II stopnia"
    elif BMI >= 30:
        return "otyłość I stopnia"
    elif BMI >= 25:
        return "nadwaga"
    elif BMI >= 18.5:
        return "waga prawidłowa"
    elif BMI >= 17:
        return "niedowaga"
    elif BMI >= 16:
        return "wychudzenie"
    else:
        return "wygłodzenie"


height = int(input("Podaj swój wzrost w cm: "))
weight = int(input("Podaj swoją wagę w kg: "))

print("Twoje BMI to ", bodyMassIndex(height, weight))
print("Interpretacja Twojego wyniku: ", interpreterBMI(bodyMassIndex(height, weight)))
