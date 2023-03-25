from lotto import get_user_numbers, check_numbers, draw_numbers

print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()
print("Podane liczby to:", user_numbers)

print("\nNaciśnij ENTER, aby dokonać losowania liczb!\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowane liczby to:", lucky_numbers)

result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("Gratulacje!!!, Jesteś milionerem!")
elif result == 5:
    print("Brawo! Trafiono piątkę, zgarniasz sporą sumkę!")
elif result == 4:
    print("Hura! Trafiono czwórkę, to całkiem niezły wynik!")
elif result == 3:
    print("Trafiono trójkę, przysługuje Ci minimalna wygrana.")
elif result in [1, 2]:
    print("Trafiono", result, "Było bardzo blisko.")
else:
    print("To nie jest Twój dzień.")
