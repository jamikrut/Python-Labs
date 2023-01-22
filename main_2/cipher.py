# napisz program ktory rozszyfruje wiadomość
# Xq|`gf(bm{|(nibfq)

# dla każdego znaku zmieniono 4 bit na przeciwny
# bity liczymy od najmniej znaczącego, 4 bit -> indeks 3

print(ord("c"))
print(chr(99))
print(bin(ord("c")))

print("{:08b}".format(ord("c")))

# 01100011 - nasza liczba
# 00011000 - maska
# 01101011 - używamy XORa (alternatywna rozłączna)

print("{:08b}".format(ord("c") ^ (1 << 3)))

msg = "Xq|`gf(bm{|(nibfq)"
for c in msg:
    print(chr(ord(c) ^ (1 << 3)), end="")
