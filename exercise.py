# students = {"Ali": 85, "Sara": 92, "Ahmed": 67, "Yasra": 98}

# a_count = 0

# for name, marks in students.items():
#     if marks >= 100:
#         grade = "A+"
#         a_count += 1
#     elif marks >= 90:
#         grade = "A+"
#         a_count += 1
#     elif marks >= 75:
#         grade = "A"
#     elif marks >= 50:
#         grade = "B"
#     elif marks <= 49:
#         grade = "F"
#     print(f"{name} got {marks} acheiving {grade}")

# print(f"{a_count} got A+")


# products = {"laptop": 1000, "mouse": 50, "keyboard": 80}

# total = 0

# while True:
#     product = input("what do you want: ")
#     if product in products:
#         price = products[product]
#         total += price
#     elif product == "done":
#         print(f"your total is {total}")
#         break
#     else:
#         print("item not available")


# 4. 🔍 Recursive Number Search:

numbers = [4, 9, 2, 7, 1]


# def find_number(lst, target):
#     if len(lst) == 0:
#         return False

#     if lst[0] == target:
#         return True

#     return find_number(lst[1:], target)


# print(find_number(numbers, 7))


# Recursive Sum of a List:


# def sum_numbers(list):
#     if len(list) == 0:
#         return f"empty array"
#     else:
#         return sum_numbers(list[1:] + list[0])


# print(sum_numbers(numbers))


# inventory system:

# inventory = {"Potion": 5, "Sword": 1, "Shield": 1}

# values = inventory.values

# print(inventory)
# objects = input("enter what you need: ")
# while True:
#     if objects in inventory:
#         if inventory[objects] == 0:
#             print("this item is finished")
#             print(inventory)
#             objects = input("enter what you need: ")
#         else:
#             inventory[objects] -= 1
#             print(
#                 f"you are using {objects} and you have only {inventory[objects]} left"
#             )
#             print(inventory)
#             objects = input("enter what you need: ")
#     elif objects == "exit":
#         print("you have left the inventory")
#         break
#     else:
#         print("not available in inventory")
#         objects = input("enter what you need: ")

# 🏆 Highest Scorer Finder:

# students = {"Ali": 85, "Sara": 92, "Ahmed": 67, "Yasra": 98}

# highest_score = 0
# achiever = ""

# for name, score in students.items():
#     if score > highest_score:
#         highest_score = score
#         achiever = name

# print(f"high score: {highest_score}")
# print(f"achiever: {achiever}")


# credentials = {"yasra": "admin", "ali": "python123", "sara": "hello"}
# attemps = 0

# while attemps < 3:
#     username = input("enter username: ")
#     if username in credentials:
#         password = input("enter password: ")
#         if password == credentials[username]:
#             print(f"hello {username}")
#             break
#         else:
#             attemps += 1
#             print("wrong password")
#     else:
#         attemps += 1
#         print("wrong username")


# 9. 🌳 Recursive String Reverser


# def reverse_word(word):
#     if len(word) == 0:
#         return ""
#     return reverse_word(word[1:]) + word[0]


# print(reverse_word("hello"))


# Product Catalog:

catalog = {
    "Laptop": {"price": 1000, "stock": 3},
    "Mouse": {"price": 50, "stock": 10},
    "Keyboard": {"price": 80, "stock": 5},
}
total = 0

while True:
    print(catalog)
    product = input("what do you need?: ")

    if product == "exit":
        print("you have left the catalog")
        break

    if product not in catalog:
        print("item not available")
        continue

    if product in catalog:
        if catalog[product]["stock"] > 0:
            catalog[product]["stock"] -= 1
            total += catalog[product]["price"]
            print(total)
            continue
        else:
            print("item out of stock")
            continue


print(f"you total is: {total}")
