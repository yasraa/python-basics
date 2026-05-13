# If Else Conditional Statements in Python | Python Tutorial - Day #14

string = "my name is yasra"
if string.find("yasra") != -1:
    print("yasra is found in the string")
else:
    print("yasra is not found in the string")

# python works on indentation and not on curly braces like in other programming languages

fruit = input("enter a fruit ")

if fruit == "apple":
    print("fruit is red")
elif fruit == "banana":
    print("fruit is yellow")
else:
    print("unknown fruit")


user = int(input("enter 1 if you are logged in"))

if user == 1:
    username = input("enter your name")
    if username == "yasra":
        print("omg yasraa u da admin")
    else:
        print("welcom ordinary person")
else:
    print("please login bitch")


marks = int(input("enter your marks: "))

if marks >= 100:
    print("you have aced")
elif marks >= 90:
    print("u got A+")
elif marks >= 75:
    print("u got A")
elif marks >= 50:
    print("u got B")
elif marks <= 49:
    print("you have failed")
else:
    print("enter a valid number")

import time

timestamp = time.strftime("%H:%M:%S")

timest = int(time.strftime("%H"))
print(timest)

if timest >= 0 and timest < 4:
    print("hey")
elif timest >= 4 and timest < 12:
    print("good morning")
elif timest >= 12 and timest < 16:
    print("good afternoon")
elif timest >= 16 and timest < 20:
    print("good evening")
elif timest >= 20 and timest < 0:
    print("good night")
else:
    print("time finish")
