from functools import reduce

# # In Python, map(), filter(), and reduce() are higher-order functions that allow you to process sequences of data elegantly without using explicit loops. While map() and filter() are natively built-in, reduce() must be explicitly imported from the standard library's functools module.🗺️ The map() FunctionThe map() function applies a transformation function to every item in an iterable and returns an iterator.Syntax: map(function, iterable)Output Size: Same number of elements as the original input.Conversion: Because it returns an iterator, you must wrap it in list() or tuple() to see the final values.python

# numbers = [1, 2, 3, 4]
# # Example: Squaring each element using a lambda function
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # Output: [1, 4, 9, 16]
# # Use code with caution.🔍 The filter() FunctionThe filter() function tests each element in an iterable against a condition (a function returning True or False) and keeps only the items that meet the criteria.Syntax: filter(function, iterable)Output Size: Equal to or smaller than the original input.Conversion: Like map(), it returns an iterator and must be converted explicitly.python

# numbers = [1, 2, 3, 4, 5, 6]
# # Example: Filtering only the even numbers
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # Output: [2, 4, 6]
# # Use code with caution.🧪 The reduce() FunctionThe reduce() function applies a function of two arguments cumulatively to sequence items from left to right, condensing the entire iterable down into a single value.Syntax: reduce(function, iterable[, initializer])Requirement: Must be imported from functools.Mechanism: It processes the first two elements, takes that result, pairs it with the third element, and repeats until one value remains.pythonfrom functools import reduce

# # numbers = [1, 2, 3, 4]
# # # Example: Multiplying all items together (1 * 2 * 3 * 4)
# # product = reduce(lambda x, y: x * y, numbers)
# # print(product)  # Output: 24
# # # Use code with caution.


# # 5. 🎓 Student Grade Converter:
# marks = [45, 67, 89, 92, 55]


# def num_conv(score):
#     if score >= 90:  # Combined your A+ checks into one condition
#         return "A+"
#     elif score >= 75:
#         return "A"
#     elif score >= 50:
#         return "B"
#     else:  # Anything under 50 falls here automatically
#         return "C"


# grade = list(map(num_conv, marks))
# print(grade)


# # 6. 🚪 Filter Active Users:
# users = [
#     {"name": "Ali", "active": True},
#     {"name": "Sara", "active": False},
#     {"name": "Ahmed", "active": True},
# ]

# active_users = list(filter(lambda user: user["active"], users))
# print(active_users)


# prices = [100, 250, 370, 150]
# total = reduce(lambda x, y: x + y, prices)
# tax_total = int(total * 1.10)
# print(tax_total)

# all_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# filter_num = list(filter(lambda x: x % 2 == 0, all_numbers))
# final = list(map(lambda x: x * x, filter_num))
# print(final)


# # 9. 🧠 is vs == Investigation:
# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)
# print(a is b)
# x = 100
# y = 100

# print(x == y)
# print(x is y)
# x = 1000
# y = 1000

# print(x == y)
# print(x is y)


# users = [
#     {"name": "Ali", "age": 30},
#     {"name": "Sara", "age": 25},
#     {"name": "Ahmed", "age": 19},
# ]

# min_age = int(input("enter your age: "))


# def check_user(x):
#     return x["age"] > min_age


# filtered_list = filter(check_user, users)

# for x in filtered_list:
#     print(f"{x['name']}")


# 12. 👑 Boss Battle: Student Report Generator:

students = [
    {"name": "Ali", "marks": 45},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 78},
    {"name": "Yasra", "marks": 88},
]

with open("file.txt", "w") as f:
    for x in students:
        f.write(f"{x['name']} : {x['marks']}\n")

total_marks = reduce(lambda x, y: x + y["marks"], students, 0)
print(total_marks)

passed_students = list(filter(lambda x: x["marks"] >= 50, students))
print(passed_students)

previous_students = list(map(lambda x: f"{x['name']} is passed", passed_students))
print(previous_students)
