# 🐍 Python “array” options

# Python actually has 2 main array-like tools:

# 1. List (most used)
# Flexible
# Dynamic size
# Mixed data types allowed
# 2. array module (rare for beginners)

# list is changeable tupl is not

# negetive indexing:
# in future if we get the question of negetive index that's how we perform it:

marks = [1, 2, 3, 4, 5, "yasra"]
# 1st we'll convert negetive indexing into positive
print(marks[-3])
# thats how it's working:
print(marks[len(marks) - 3])
print(marks[5 - 3])

if "yasra" in marks:
    print("yasra is in the list")
else:
    print("yasra is not in the list")

if "asr" in "yasra":
    print("asr is in the string")
else:
    print("asr is not in the string")


# printing element in the specific range:
print(marks[1:4])

numbers = [1, 2, 3, 4, 5, 6, 76, 5, 4545, 34, 645, 56, 54, 456, 5, 634, 6, 4, 5]

# printing element in a specific range
print(numbers[2:15])
# the last value is for jump
print(numbers[2:15:3])


# list comprehension:
# list comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition
# Example:
# squares = [x**2 for x in range(10)]
# This creates a list of squares for numbers from 0 to 9.
squares = [x * x for x in range(10)]
print(squares)


# list methods:
# append() - adds an element to the end of the list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.append(11)
print(l)
# sort() - sorts the list in ascending order
n = [5, 2, 9, 1, 5, 6, 3, 2]
n.sort()
print(n)
n.sort(reverse=True)
print(n)
# reverse() - reverses the order of the list
n.reverse()
print(n)
# count() - counts the number of occurrences of an element in the list
print(n.count(5))
# copy() - creates a shallow copy of the list
n_copy = n.copy()
print(n_copy)
# extend() - extends the list by appending elements from another iterable
n.extend([7, 8, 9])
print(n)
# index() - returns the index of the first occurrence of an element in the list
print(n.index(5))
# insert() - inserts an element at a specified position in the list
n.insert(0, 0)
print(n)

# concatenation of list:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)
