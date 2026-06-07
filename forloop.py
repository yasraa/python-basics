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

# juice machine:

# question = str(input("Do you want juice? yes/no: "))
# attempt = 0

# while attempt < 3:
#     if question == "yes":
#         print("juice pouring")
#         question = str(input("Do you want juice? yes/no: "))
#         attempt += 1
#     elif question == "no":
#         print("ok")
#         break
#     else:
#         print("invalid input")

# shopping cart calculator:

# total = 0

# while True:
#     price = input("enter price: ")

#     if price == "done":
#         break

#     total += float(price)

# print("total price:", total)

username = "yasra"
password = "admin"
userinput = input("enter username: ")
attempt = 0

while attempt < 3:
    if userinput == username:
        inputpassword = input("enter password: ")
        if inputpassword == password:
            print("you are logged in")
            break
        else:
            print("wrong password")
            attempt += 1
    else:
        print("wrong username")
        attempt += 1
        userinput = input("enter username: ")
else:
    print("too many attempts, try again later")

# Break and continue:
# break will skip the loop
# continue will skip the current iteration and move to the next one
