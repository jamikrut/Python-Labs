'''Moduł do obsługi list liczb całkowitych. '''


def is_integer(myList):
    ''' Funkcja weryfikuje czy podana lista zawiera wyłącznie liczby całkowite. '''
    list_check = 1
    for number in myList:
        if isinstance(number, int) == True:
            list_check *= 1
        else:
            list_check *= 0
    if list_check == 1:
        return True
    else:
        return False


def sum_elements(myList):
    ''' Funkcja sumuje wszystkie liczby z podanej listy. '''
    sum = 0
    for element in myList:
        sum += element
    return sum


def multiply_elements(myList):
    ''' Funkcja mnoży wszystkie liczby z podanej listy. '''
    product = 1
    for element in myList:
        product *= element
    return product


if __name__ == "__main__":
    myList = [1, 2, 3.2]
    print(is_integer(myList))
    print(sum_elements(myList))
