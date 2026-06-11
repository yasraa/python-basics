# f = open("myfile.txt", "r")
# text = f.read()
# print(text)
# f.close()


# # to create a file and write to it
# f = open("mynewfile.txt", "w")
# f.write("Hello, this is a new file.")
# f.close()


# # write vs append
# # using "w" will overwrite the existing content of the file
# f = open("mynewfile.txt", "w")
# f.write("This will overwrite the existing content.")
# f.close()
# # using "a" will append to the existing content of the file
# f = open("mynewfile.txt", "a")
# f.write("\nThis will be appended to the existing content.")
# f.close()


# # rb and wb are used for reading and writing binary files, respectively. For example, to read a binary file:
# f = open("mynewfile.txt", "rb")
# binary_data = f.read()
# print(binary_data)
# f.close()


# # with statement is used to automatically close the file after the block of code is executed
# with open("myfile.txt", "r") as f:
#     text = f.read()
#     print(text)


f = open("myfile.txt", "r")
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()
