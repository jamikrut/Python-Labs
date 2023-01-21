sum = 1
count = 1
for i in range(2, 8 ** 2 + 1, 1):
    count = count * 2
    sum = sum + count
print("Suma ziaren na szachownicy to " + str(sum) + ".")

#ziarno ma 0,4mg
print("Suma ziaren to " + str(sum*0.4/(10e9)) + " ton.")

#szacunkowa roczna produkcja 782 mln ton (2022)
print("Jest to " + str((sum*0.4/(10e9))/782e6) + " światowej rocznej produkcji.")
