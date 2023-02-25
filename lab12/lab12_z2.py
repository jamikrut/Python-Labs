# Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998.

def perimeter(a, b):
    return print("Obwód prostokąta o bokach", a, "i", b, "wynosi", 2 * a + 2 * b)


def area(a, b):
    return print("Pole powierzchni prostokąta o bokach", a, "i", b, "wynosi", a * b)


def diagonal(a, b):
    return print("Długość przekątnej prostokąta o bokach", a, "i", b, "wynosi", (a ** 2 + b ** 2) ** 0.5)


# Prostokąt o bokach 4 i 5
perimeter(4, 5)
area(4, 5)
diagonal(4, 5)

print()
# Prostokąt o bokach 2678 i 5678
perimeter(2678, 5678)
area(2678, 5678)
diagonal(2678, 5678)

print()
# Prostokąt o bokach 344555 i 788998
perimeter(344555, 788998)
area(344555, 788998)
diagonal(344555, 788998)
