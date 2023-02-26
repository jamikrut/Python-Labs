def scope_test():
    x =123
    print("W środku funkcji " + str(x))

x = 99
scope_test()
print("na zewnątrz "+ str(x))