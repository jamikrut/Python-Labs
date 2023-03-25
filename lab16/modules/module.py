''' to jest nasz pierwszy własny moduł '''


def is_string(val):
    ''' simple string value validator '''
    return isinstance(val, str)


def sum_list_elem(list):
    sum = 0
    for i in list:
        sum += i
    return sum


if __name__ == "__main__":
    print(is_string("haha")) == True
    print(is_string(123)) == False
