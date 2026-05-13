# match case is a new feature in python 3.10 that allows us to match patterns in a more concise and readable way. It is similar to switch case statements in other programming languages.
# syntax:
# match variable:
#     case pattern1:
#         # code to execute if pattern1 matches
#     case pattern2:
#         # code to execute if pattern2 matches
#     case _:
#         # code to execute if no pattern matches


fruit = input("enter a fruit ")
match fruit:
    case "apple":
        print("fruit is red")
    case "banana":
        print("fruit is yellow")
    case _:
        print("unknown fruit")

# we can also use match case with if statements to create more complex patterns

user = int(input("enter 1 if you are logged in"))
match user:
    case 1:
        username = input("enter your name")
        match username:
            case "yasra":
                print("omg yasraa u da admin")
            case _:
                print("welcom ordinary person")
    case _:
        print("please login")


# 🍔 Food Ordering System Using match-case

food_item = input("enter item : ").lower()
match food_item:
    case "burger":
        print("burger costs 5$")
    case "pizza":
        cheese = input("do you want cheese on your pizza? (yes/no) ")
        if cheese == "yes":
            print("pizza costs 750")
        else:
            print("pizza costs 700")
    case "salad":
        print("healthy choice!")
    case "fries" | "chips":
        print("crispy sides added")
    case "water" | "juice" | "soda":
        print("drink added")
    case "ice creame":
        print("desert added!")
    case _ if food_item.isalnum():
        print("don not use numbers or special characters in the item name")
    case _:
        print("item not found in menu")
