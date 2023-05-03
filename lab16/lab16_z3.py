from lotto import get_user_numbers, check_numbers, draw_numbers

print("Witaj w grze lotto!")
user_numbers = get_user_numbers()
print("Podane liczby to:", user_numbers)

print("\nNaciśnij ENTER aby dokonać losowania liczb!")
input()
lucky_numbers = draw_numbers()
print("Wylosowane liczby to:", lucky_numbers)

result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("Gratulacje!!!", "Jesteś milionerem!!!")
elif result == 5:
    print("Brawo!", "Trafiono piątkę! Zgarniesz sporą sumkę.")
elif result == 4:
    print("Hurra!", "Trafiono czwórkę!", "To całkiem niezły wynik!")
elif result == 3:
    print("Trafiono trójkę.", "Przysługuje Ci minimalna wygrana.")
elif result in (1, 2):
    print("Trafiono ", result, ".", "Było bardzo blisko.", sep="")
else:
    print("Nic nie trafiono.", "To nie jest Twój dzień.")
