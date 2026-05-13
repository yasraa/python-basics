# you can loop on any iterable object, such as a list or a string
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# name = "yasra"
# for i in name:
#     print(i)
#     if i == "r":
#         print("this is special")

# colors = ["pink", "yellow", "green"]
# for x in colors:
#     print(x)
#     for ind in x:
#         print(ind)

# Range

# for number in range(6):
#     print(number)

# for number in range(
#     2, 6
# ):  # first value define starting point second will end point but a number less like if you give 9 it will give 7.
#     print(number)

# for loop

# A for loop is used when you already know what you want to loop through.

# Example:

# fruits = ["apple", "banana", "mango"]

# for fruit in fruits:
#     print(fruit)

# Python automatically goes item by item:
# 🍎 → 🍌 → 🥭

# You don’t manage the counting yourself.

# while loop

# A while loop keeps running until a condition becomes False.

# Example:

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# This keeps asking:

# “Is condition still True?”

# If yes → run again 🔄


i = 0
while i < 5:
    print(i)
    i += 1


# password checker:
# password = str(input("enter your password: "))
# while password != "qwerty":
#     if password == "exit":
#         print("loop is broken")
#         break

#     print("wrong password")
#     password = str(input("enter your password: "))
# else:
#     print("logged in")


# WORD GUESSER GAME:

# word = str(input("guess the word: "))

# while word != "yasraqt":
#     print("wrong word")
#     word = str(input("guess the word: "))
# print("congrats")


# Break and continue:
# break will skip the loop
# continue will skip the current iteration and move to the next one
