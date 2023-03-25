# Korzystając z odpowiednich modułów napisz skrypt realizujący następujące zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

import platform

print("Nazwa procesora to:")
print(platform.processor())
print()

import random

print("3 niepowtarzalne liczby ze zbioru 1-10:")
print(random.sample([i for i in range(1, 11)], 3))
print()

import math

print("Sinus kąta 90 stopni:")
print(math.sin(math.radians(90)))

# help(math.sin)
# print(dir(random))
