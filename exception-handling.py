# exception handling in python is done using try-except blocks. The try block contains code that may raise an exception, while the except block contains code that will be executed if an exception occurs. You can also use finally block to specify code that will be executed regardless of whether an exception occurred or not.
try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = num1 / num2
    print(f"the result is {result}")
except exception as e:
    print(f"an error occurred: {e}")

print("program continues after exception handling")


# finally block is used to specify code that will be executed regardless of whether an exception occurred or not. It is typically used for cleanup actions, such as closing files or releasing resources.
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("file not found")
finally:
    print("this will always be executed")


# but the last statemnt of print will still work without finally block the real use of finally block is we can see in the fuctions when we want to return a value from the function but we also want to execute some code before returning the value we can use finally block to execute that code before returning the value.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "cannot divide by zero"
    finally:
        print("this will always be executed")


print(divide_numbers(10, 2))
print(divide_numbers(10, 0))

# now this time the last print statement in function will not work without finally block


# custom error handling:

age = int(input("enter your age: "))
if age < 0:
    raise ValueError("age cannot be negative")
elif age < 18:
    raise ValueError("you must be at least 18 years old")
else:
    print("you are eligible to vote")
