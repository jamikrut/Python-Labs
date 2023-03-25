# Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem cezara z parametrem przesunięcia równym 3.
# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

message = "VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ"
cracked_message = ""

ALPHABET = ""

for i in range(ord("A"), ord("Z") + 1):
    ALPHABET += chr(i)

''' nieptymalny sposób - bez słownika
for letter in message:
    if letter in ALPHABET:
        cracked_letter = chr(ord(letter) - 3)
    else:
        cracked_letter = letter
    cracked_message += cracked_letter

print(cracked_message)
'''


# z użyciem słownika
def decipher_function():
    ALPHABET = ""
    for i in range(ord("A"), ord("Z") + 1):
        ALPHABET += chr(i)

    cipher = {}
    for letter in ALPHABET:
        cipher[letter] = chr(ord(letter) - 3)
    cipher["B"] = "Y"
    return cipher


cracked_message2 = ""
for letter in message:
    if letter in ALPHABET:
        cracked_message2 += str(decipher_function().get(letter))
    else:
        cracked_message2 += letter

print("Rozszyfrowana wiadomość:")
print(cracked_message2)
