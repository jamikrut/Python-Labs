numbers = [10, 8, 6, 4, 2]

print(5 in numbers)
print(7 not in numbers)
del numbers

numbers = [i for i in range(1, 1001)]
# to samo co wrzucanie pętlą

del numbers
numbers = [i ** 2 for i in range(1, 101)]
print(numbers)

# teraz z instrukcją warunkową
del numbers
numbers = [i ** 2 for i in range(1, 101) if i % 2 == 0]
print(numbers)

# ile jest liczb w przedziale od 1 do 300 które dzielą się przez 3 i 7
del numbers
numbers = [i for i in range(1, 301) if (i % 3 == 0) and (i % 7 == 0)]
print(numbers)