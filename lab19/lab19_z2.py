class Stack():

    def __init__(self):
        self.__stack_list = []

    def push_numbers(self):
        self.__stack_list.append([i for i in range(1,101)])
        return self.__stack_list

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def push_value(self, val):
        self.__stack_list.append(val)
        return val

# -----------------------------------------------------------


object1 = Stack()
object2 = Stack()
object3 = Stack()


print(object1.push_numbers())

val = object1.pop()
print(object2.push_value(val))

