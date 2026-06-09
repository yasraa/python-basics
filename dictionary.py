# # dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
# # Dictionaries are defined using curly braces {} with key-value pairs separated by a colon :.
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict)
# print(type(my_dict))
# print(
#     my_dict["name"]
# )  # Accessing value by key if the key does not exist it will raise a KeyError
# print(
#     my_dict.get("age")
# )  # Accessing value using get() method if the key does not exist it will return None instead of raising an error

# print(
#     my_dict.keys()
# )  # Returns a view object that displays a list of all the keys in the dictionary
# print(my_dict.values())  # Returns a view object that displays a list of all the values

# for key in my_dict:
#     print(key)  # Iterating through keys


# # to update the value of a key in the dictionary, you can simply assign a new value to that key.
# my_dict["age"] = 31
# print(my_dict)


student = {"name": "Yasra", "age": 19, "course": "Python"}

for key, value in student.items():
    print(f"{key}:{value}")


products = {"Laptop": 1000, "Mouse": 50, "Keyboard": 80}

product = input("search product: ")
if product in products:
    price = products[product]
    print(f"available the price is {price}")
else:
    print("not available")


# login system
credentials = {"yasra": "admin", "ali": "python123"}
username = input("enter username: ")
if username in credentials:
    password = input("enterpassword: ")
    if password in credentials[username]:
        print("you are logged in")
    else:
        print("wrong pasword")
else:
    print("invalid credentials")


# set methods:
# update() method is used to update the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.
ep1 = {"name": "Yasra", "age": 19}
ep2 = {"course": "Python", "grade": "A"}
ep1.update(ep2)

# pop() method is used to remove the specified key and return the corresponding value. If the key is not found, it raises a KeyError.
removed_value = ep1.pop("age")
print(removed_value)
print(ep1)

# clear() method is used to remove all items from the dictionary.
ep1.clear()
print(ep1)

# del() method is used to delete a key-value pair from the dictionary. If the key is not found, it raises a KeyError.
del ep2["grade"]
print(ep2)
