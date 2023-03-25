# Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1 }.

def how_many_times_occur(string):
    occurs = {}
    for letter in string:
        occurs[letter] = string.count(letter)
    return occurs


print(how_many_times_occur("abracadabra"))
