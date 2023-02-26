# Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

# 1 * 1
# 1 * 2
# 1 * 3

def multiplication(base, multiplier):
    if multiplier == 1:
        return base
    if multiplier == 2:
        return base * multiplier

    return base + multiplication(base, multiplier - 1)


for n in range(1, 10):
    print("Tabliczka mnożenia dla " + str(n) + ":")
    for i in range(1, 10):
        print(n, "*", i, "=", multiplication(n, i))
    print()
