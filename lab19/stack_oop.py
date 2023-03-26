class Stack():  # definiujemy klasę stosu
    def __init__(self):  # definiujemy konstruktor
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class StackSum(Stack):
    def __int__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


# ----------------------------------------------------

obj = Stack()
obj2 = Stack()

print("Umieszczamy elenty ma stosie")

obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

# obj.__stack_list = [4, 4, 4]
# print(len(obj.__stack_list))

print(obj2.pop())
print(obj2.pop())
print(obj2.pop())
print()

print(obj.pop())
print(obj.pop())
print(obj.pop())
print()

print("stos 1", obj.get_sum())
print("stos 2", obj2.get_sum())
