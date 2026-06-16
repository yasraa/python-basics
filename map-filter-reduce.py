import reduce

# In Python, map(), filter(), and reduce() are higher-order functions that allow you to process sequences of data elegantly without using explicit loops. While map() and filter() are natively built-in, reduce() must be explicitly imported from the standard library's functools module.🗺️ The map() FunctionThe map() function applies a transformation function to every item in an iterable and returns an iterator.Syntax: map(function, iterable)Output Size: Same number of elements as the original input.Conversion: Because it returns an iterator, you must wrap it in list() or tuple() to see the final values.python

numbers = [1, 2, 3, 4]
# Example: Squaring each element using a lambda function
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
# Use code with caution.🔍 The filter() FunctionThe filter() function tests each element in an iterable against a condition (a function returning True or False) and keeps only the items that meet the criteria.Syntax: filter(function, iterable)Output Size: Equal to or smaller than the original input.Conversion: Like map(), it returns an iterator and must be converted explicitly.python

numbers = [1, 2, 3, 4, 5, 6]
# Example: Filtering only the even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
# Use code with caution.🧪 The reduce() FunctionThe reduce() function applies a function of two arguments cumulatively to sequence items from left to right, condensing the entire iterable down into a single value.Syntax: reduce(function, iterable[, initializer])Requirement: Must be imported from functools.Mechanism: It processes the first two elements, takes that result, pairs it with the third element, and repeats until one value remains.pythonfrom functools import reduce

numbers = [1, 2, 3, 4]
# Example: Multiplying all items together (1 * 2 * 3 * 4)
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
# Use code with caution.
