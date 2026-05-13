 import pandas

# # to check if our pandas installation is working:
print(pandas.__version__)
print("Hello world")

# # to use double quotes in a string we use achracter \ before the double quotes:
print('I am learning "Python" programming language')
# # to use backslash in a string we use character \ before the backslash:
 print("This is a backslash: \\")
# # to use new line in a string we use character \ before the n:
 print("This is the first line.\nThis is the second line.")
# # to use single quote in a string we use character \ before the single quote:
 print("It's a nice day!")

# # properties of print function:

# # to print multiple items in a single line we can use comma to separate them and can use a seperator aswell:
 print("Hello", "World", "earth", "sun", sep="-")

# # data types in python:

 a = 10  # integer
 b = 3.14  # float
 c = "Hello"  # string
 d = True  # boolean
 e = None  # NoneType
 f = complex(2, 3)  # complex number
 g = [
     1,
     2,
     ["apple", "banana"],
 ]  # list is an ordered collection of data which is mutable and can contain duplicate elements
 h = (
     ("sparrow", "lion"),
     ("elephant", "giraffe"),
     3,
 )  # tuple are same but they are immutable and cannot change after creation like lists
 i = {
     "name": "Alice",
     "age": 30,
 }  # dictionary is a collection of key-value pairs which is unordered and mutable
 print(type(a))
 print(type(b))
 print(type(c))
 print(type(d))
 print(type(e))
 print(type(f))
 print(type(g))
 print(type(h))
 print(type(i))


# # arithmetic operators in python:
 x = 2
 y = 3
 print(x + y)  # addition
 print(x - y)  # subtraction
 print(x * y)  # multiplication
 print(x / y)  # division
 print(x // y)  # floor division
 print(x % y)  # modulus
 print(x**y)  # exponentiation


# # typecasting in python:
 num1 = "10"
 num2 = "20"
# # to convert string to integer we use int() function:
 num1 = int(num1)
 num2 = int(num2)
 print(num1 + num2)  # now we can add them as integers

 a = 1
 b = 5
 total = a + b
 conversion = str(total)
# # to convert integer to string we use str() function
 print(conversion)
 print(type(conversion))


# # taking input in python:
 a = input("Enter num1: ")
 b = input("Enter num2: ")
 total = a + b
 print(
     "The total is: " + total
 )  # this will concatenate the strings instead of adding them as numbers
 # to fix this we need to convert the inputs to integers:
 a = int(input("Enter num1: "))
 b = int(input("Enter num2: "))
 total = a + b
 print(
     "The total is: " + str(total)
 )  # now we can add them as numbers and convert the result to string for printing


# # strings in python:
# # to create multiple line string we can use triple quotes:
# multi_line_string = """This is a multi-line string.
# It can span multiple lines.
# We can use it for long text."""
 print(multi_line_string)

# # to access individual characters in a string we can use indexing:
 my_string = "Hello, World!"
 print(my_string[0])  # H
 print(my_string[7])  # W
 print(my_string[-1])  # !

# # if i used ,y_string[0:4] it will give me the characters from index 0 to 3 (4 is not included):

# for char in my_string:
#     print(char)

#     # that's how we can slice negetive numbers:
#     nm = "Harry"
# # print(nm[-4:-2])
# # *The length of the string is 5, and the order of characters starts from zero, so H(0), a(1), r(2), r(3), y(4).
# # Back to the code;
# # (len(nm)-4-->5-4=1
# # (len(nm)-2-->5-2=3
# # *Hypothetically new statement is print(nm[1:3])
# # we know the starting point is 1, but to access the character's order we use n-1 principle.
# #  So, order of character=n-1
# # OC=3-1=2
# # Take the order of characters from 1 to 2 from the actual string; hence, the output is (ar).


 name = "yasra"
 upper_name = name.upper()
 print(upper_name)


# # rstrip removes any trailing characters:
 name = "yasra$$$!!"
 clean_name = name.rstrip("!")

 print(clean_name)


# you can replace occurences of a substring with another substring using the replace() method:
text = "I like apples. Apples are my favorite fruit."
new_text = text.replace("apples", "oranges")
print(new_text)

# string.split splits the string at the given alphabet (and spaces) and returns a list of items

name = "my name is yasra"
splitted = name.split(
    " "
)  # as i've only gave this space and not any character my string will split where are spaces and become an array"
print(splitted)
print(type(splitted))


# you can capatialize using the capitalize() method:
# it turn only first letter capital and the rest will be small letters:
blog_heading = "yasra"
capitalized_heading = blog_heading.capitalize()
print(capitalized_heading)

# with the help of center() method we can center align the string within a specified width (we have to provide parameter):
heading = "hello welcome to my blog"
centered_heading = heading.center(50)
print(centered_heading)

# you can count the number, chracters or words in a string using count():
sentence = "I have a cat. My cat is cute."
cat_count = sentence.count("cat")
print(cat_count)

# to check if a string starts with a specific substring we can use startswith() method:
greeting = "Hello, how are you?"
print(greeting.startswith("Hello"))  # True
print(greeting.startswith("Hi"))  # False

# to check if a string ends with a specific substring we can use endswith() method:
filename = "report.pdf"
print(filename.endswith(".pdf"))  # True
print(filename.endswith(".docx"))  # False

# string.find( will return the first occurence of the character or word you are findin and give its index:
paragraph = "Python is a great programming language. I love learning Python."
index = paragraph.find("Python")
# and if it coudn't find any occurence it will return -1
print(index)
# index() method is same as find() but the only difference is if it does'nt find any occurrences it will give an error and exit instead of returning -1 like find()


# to find if our is string is alphanumeric or not we use isalnum() method:
string1 = "Hello123"
string2 = "Hello 123"
print(string1.isalnum())  # True
print(string2.isalnum())  # False (because of the space)
# isalpha is same but only gives true when the string is consist of alphabets only


# is printable() checks if the characters are printable or not
 string= "this is printable \n" # false because new line char is'nt printable
 string2 =" this is printable "  # will return true
print(string.isprintable())
print(string2.isprintable())


# 18 string.isspace checks if any space bar has been used in the string
# 19.string.istitle The istitile() returns True only if the first letter of each word of the string is capitalized, else 20. string.isupper checks if all characters are uppercase in a string
# 21. string.startswith checks if a string starts with a given value
# 22. string.swapcase convert uppercase to lowercase and vice versa in a string
# 23.string.title converts first character of all the words in the sentence to capital