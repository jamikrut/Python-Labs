# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

def numbers_to_power(numbers, power):
    return [i ** power for i in numbers]


print(numbers_to_power([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
