# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak,
# dowolną ilość razy, w poziomie lub w pionie.

def printChar(char, lenght, horizontal=True):
    if horizontal:
        print(char * lenght)
    else:
        print((char + "\n") * lenght)


printChar("#", 6, horizontal=False)
