print("Podaj zakres liczb do wyświetlenia: ")
r1 = int(input("Zakres od: "))
r2 = int(input("Zakres do: "))
print("Liczby podzielne podzielne przez 3, 5 lub 7 z zakresu od " + str(r1) + " do " + str(r2) + " to: ")
for i in range(r1, r2 + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
