class Book:
    def __int__(self, title, autor, date, publisher):
        self.__title = title
        self.__autor = autor
        self.__date = date
        self.__publisher = publisher

    def gettitle(self):
        return self.__title

    def getautor(self):
        return self.__autor

    def getdate(self):
        return self.__date

    def publisher(self):
        return self.__publisher


books = []
books.append(Book("Uczenie maszynowe w Pythonie - Leksykon kieszonkowy", "Harrison, Matt", "Helion", 2020))
books.append(Book("Praktyczna inżynieria wsteczna - Metody, techniki i narzędzia", "Jurczyk, Mateusz", "PWN", 2016))
