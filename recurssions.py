# a function called in a function is called recursion:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequence(n - 1) + sequence(n - 2)


print(sequence(6))
