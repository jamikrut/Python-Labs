# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
# Uwzględnij możliwość pomyłki użytkownika.

def get_float():
    counter = 0
    floatNumbers = []
    while counter < 3:
        try:
            arg = float(input("Podaj liczbę zmiennoprzecinkową: "))
            floatNumbers.append(arg)
            counter += 1
        except ValueError:
            print("Podano błędną wartość. Spróbuj jeszcze raz.")
        except:
            print("Nieznany błąd.")
    return floatNumbers


print(get_float())
