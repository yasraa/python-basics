# global vs local variable
a = 10  # global variable


def fun():
    a = 20  # local variable
    print("inside function", a)


fun()
print("outside function", a)


# to access global variable inside function we can use global keyword
def fun1():
    global a
    a = 30  # this will change the global variable
    print("inside function", a)


fun1()
print("outside function", a)
