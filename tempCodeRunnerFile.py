# the syntax of functions in python is as follows:
# # def function_name(parameters):
# #     # function body
# #     return value
# # Example:
# # def greet(name):
# #     return f"Hello, {name}!"
# # print(greet("Alice"))


# def greet(name):
#     return f"god morning,{name}!"


# print(greet("yasra"))


# # to add two numbers:


# def add(a, b):
#     return a + b


# print(add(1, 2))


# # age checker minor/adult

# age = int(input("enter your age "))


# def agechecker():
#     if age >= 18:
#         status = "adult"
#     else:
#         status = "minor"
#     return status


# print(agechecker())


# # number checker even/odd:


# number = int(input("enter a number"))


# def number_checker():
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# print(number_checker())


# # voucher checker:


# def voucher_checker(total):
#     if total >= 1000:
#         voucher = input("enter voucher: ")
#         if voucher == "478fd":
#             discounted_price = total * 0.9
#             return discounted_price
#         else:
#             return f"voucher incorrect"
#     else:
#         return f"you are not elegible"
#     return total


# final_price = voucher_checker(1300)
# print(final_price)


# def shopping_cost(total):
#     if total >= 5000:
#         print("you are going to get free shipping ")
#         return total
#     else:
#         print("yout final price after adding shipment is ")
#         return total + 250


# final_price = shopping_cost(323)
# print(final_price)
