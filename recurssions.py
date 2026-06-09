# # a function called in a function is called recursion:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))


# def sequence(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return sequence(n - 1) + sequence(n - 2)


# print(sequence(6))


# # revese number without using a loop


def countdown(n):
    if n == 1:
        return 1
    else:
        print(n)
        return countdown(n - 1)


print(countdown(5))
print("times up")


# recursive functions to add numbers:


def counter(n):
    if n == 0:
        return 0
    else:
        print(n)
        return counter(n - 1) + n


print(counter(30))
