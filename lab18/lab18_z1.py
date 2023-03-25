# Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi) wraz z punktami kodowymi dla każdej litery.

alphabet = ""

for i in range(ord("a"), ord("z") + 1):
    alphabet += chr(i)

print(alphabet)

alphabet_pl = alphabet + "ąćęółńźż"

for letter in alphabet_pl:
    print(letter, ord(letter))
