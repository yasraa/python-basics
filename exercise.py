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


def sum_numbers(list):
    if len(list) == 0:
        return f"empty array"
    else:
        return sum_numbers(list[1:] + list[0])


print(sum_numbers(numbers))
