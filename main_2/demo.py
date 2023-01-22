# jeżeli temperatura bedzie ujemna lub będzie pochmurno
# to zostaniemy w domu, a jeżeli nie to pójdziemy na spacer

temperature = -5
is_sun_shining = False

if temperature < 0 or not is_sun_shining:
    print("Zostajemy w domu")
else:
    print("Idziemy na spacer")

# wyświetl cyfrę, chyba że ...
# liczba parzysta lub liczba większa od 6 to wyświetli gwiazdkę
for i in range(10):
    if i > 6 or i % 2 == 0:
        print("*", end=" ")
    else:
        print(i, end=" ")

#