# Napisz funkcję usuwającą duplikaty z dowolnej listy elementów.
#
# Przykład:
# print(remove_duplicates(["Ala", "Zosia", "Zosia", "Marek"]))
# ["Ala", "Zosia", "Marek"]


def remove_duplicates(myList):
    myListWithoutDuplicates = []
    for element in myList:
        if element not in myListWithoutDuplicates:
            myListWithoutDuplicates.append(element)
    return (myListWithoutDuplicates)


myList = ["Ala", "Zosia", "Zosia", "Marek"]
print(remove_duplicates(myList))
