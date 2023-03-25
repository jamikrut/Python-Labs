# Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
# • stwórz modułu o dowolnej nazwie,
# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
# • dodaj funkcję sumującą wszystkie liczby z listy,
# • dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
# • zaimportuj utworzony moduł i skorzystaj z jego funkcji.

import integers

mojaLista1 = [1, 9, 81]
mojaLista2 = [1, 9.2, 81]

print("Czy lista", mojaLista1, "zaiera tylko liczby całkowite:", integers.is_integer(mojaLista1))
print("Czy lista", mojaLista2, "zaiera tylko liczby całkowite:", integers.is_integer(mojaLista2))

print("Suma elementów", mojaLista1, "to", integers.sum_elements(mojaLista1))
print("Suma elementów", mojaLista2, "to", integers.sum_elements(mojaLista2))

print("Iloczyn elementów", mojaLista1, "to", integers.multiply_elements(mojaLista1))
print("Iloczyn elementów", mojaLista2, "to", integers.multiply_elements(mojaLista2))
