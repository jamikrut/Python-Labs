class Employee:
    def __int__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname + " " + self.__lastname

    def getage(self):
        return self.__age



employess = []
employess.append(Employee("Jan", "Kowalski", 25, 3800))
employess.append(Employee("Natalia", "Nowak", 60, 15200))