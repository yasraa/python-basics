# how import works in py:
# import math
# print(math.sqrt(16))


# we can also import specific functions from a module:
#  from math import sqrt
#  print(sqrt(16))


# we can also import a function and give it an alias:
# from math import sqrt, pow as p
# print(sqrt(16))
# print(p(2, 3))

# dir() function is used to get the list of all the functions and variables in a module:
# import math

# print(dir(math))

# you can also import your own modules:

from yasra import welcome as w

if __name__ == "__main__":
    print(__name__)
    w("yaa")
