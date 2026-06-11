# 1. 📖 Dictionary Methods Practice:
student = {"name": "Yasra", "age": 19, "course": "Python"}

print(student.keys())

print(student.values())

for key, value in student.items():
    print(f"{key}:{value}")

new = {"city": "karachi"}
student.update(new)
print(student)

if "age" in student:
    print("age exists")
else:
    ("nos")


# 3. 🎯 for-else Challenge

numbers = [4, 8, 15, 16, 23, 42]

num = int(input("enter a number"))

for i in numbers:
    if num in numbers:
        print("found")
        break
else:
    print("not available")

users = ["Ali", "Sara", "Ahmed", "Yasra"]
user = input("enter a username: ")
for i in users:
    if user in users:
        print("found")
else:
    print("no user")


# 5. 🧮 Exception Handling:

try:
    num1 = int(input("enter num 1: "))
    num2 = int(input("enter num 2: "))
    result = num1 / num2
    print(f"the result is{result}")
except (ValueError, ZeroDivisionError) as e:
    print(e)
except Exception as e:
    print(f"an error occurred: {e}")
finally:
    print("this will always be executed")


# 7. 🔐 PIN Validator:

try:
    pin_input = input("enter 4 digit pin: ")
    if len(pin_input) != 4:
        raise ValueError("pin limit is 4 digit")
    else:
        pin = int(pin_input)
        print(pin)
except Exception as e:
    print(e)


# 10. 🏦 ATM Withdrawal
try:
    balance = 5000
    withdrawal = int(input("enter withdrawal amount: "))

    if balance > withdrawal and withdrawal > 0:
        balance -= withdrawal
        print("withdrawal successfull")
        print(f"you have {balance} rupees left")
    else:
        raise ValueError("insufficient amount or invalid withdrawal")

except Exception as e:
    print(e)


# Create a menu-driven banking system:

details = {"balance": 5000, "pin": 2456}
options = ["check balance", "withdraw", "deposit", "exit"]


def preview_menu():
    for index, menu in enumerate(options):
        print(f"{index}:{menu}")


try:
    while True:
        preview_menu()
        action = int(input("enter what do you want: "))
        if action == 3:
            break
        elif action == 0:
            print(f"you total balance is {details['balance']}")
        elif action == 1:
            withdrawal = int(input("enter withdrawal amount: "))
            if details["balance"] > withdrawal and withdrawal > 0:
                details["balance"] -= withdrawal
                print("withdrawal successfull")
                print(f"you have {details['balance']} rupees left")
            else:
                raise ValueError("insufficient amount or invalid withdrawal")
        elif action == 2:
            deposit = int(input("enter deposit amount: "))
            if deposit > 0:
                details["balance"] += deposit
                print("deposit successfull")
                print(f"you have {details['balance']} rupees in your account")
            else:
                raise ValueError("invalid deposit amount")

except Exception as e:
    print(e)
