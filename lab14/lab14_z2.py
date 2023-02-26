# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def add_unique_elements(lll):
    for n in range(3):
        for i in range(0, len(lll)):
            if lll[i] not in list:
                list.append(lll[i])


list1 = [1, 2]
list2 = [1, 1]
list3 = [4, 4, 4]

add_unique_elements(list1)

list = []

#list = [i for i in list1 if list1[i] not in list]




print(list)
