a = 5
b = 3

# koniunkcja bitowa
print(a, "&", b, "=", a & b)

# print(bin(a))
# print(bin(b))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a & b))

print("")

# alternatywa bitowa
print(a, "|", b, "=", a | b)

# print(bin(a))
# print(bin(b))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a | b))

print()

# xor
print(a, "^", b, "=", a ^ b)

# print(bin(a))
# print(bin(b))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a ^ b))

print()

# przesunięcie bitowe w prawo
print(a, ">>", b, "=", a >> b)

# print(bin(a))
# print(bin(b))
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a >> b))

print()

# przesunięcie bitowe w lewo
print(a, "<<", b, "=", a << b)

# print(bin(a))
# print(bin(b))
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a << b))

print()

# negacja bitowa
print("~" + str(a), "=", a << b)


print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))

print(0b11111111)