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
