import random

throws = []
count = 0

for i in range(16):
    result = random.randint(1, 6)
    throws.append(result)
    if result == 6:
        count += 1

print("Oto wyniki rzutów kostką:", throws)
print("Za 8 razem wypadł wynik:", throws[7])
print("Wynik 6 padł " + str(count) + " razy.")

'''
m_count = 1
for j in range(0,14):
    if throws[j] == throws[j+1]
        m_count += 1
    else:
        m_count = 1

'''