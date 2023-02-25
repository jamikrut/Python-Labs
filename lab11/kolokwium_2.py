# Pobierz od użytkownika trzy liczby całkowite reprezentujące długości odcinków i sprawdź czy jest możliwe zbudowanie z tych odcinków dowolnego trójkąta.

a = int(input("Podaj długość pierwszego odcinka: "))
b = int(input("Podaj długość drugiego odcinka: "))
c = int(input("Podaj długość trzeciego odcinka: "))

if (a > b + c) or (b > a + c) or (c > a + b):
    print("Z tych odcinków można zbudować trójkąt.")
else:
    print("Z tych odcinków nie można zbudować trójkąta.")
