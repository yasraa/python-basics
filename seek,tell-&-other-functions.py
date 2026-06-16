# # The Python seek() method changes the position of the file pointer (cursor) inside an open file stream to a specific location. This allows you to randomly access, read, or write data anywhere within the file instead of processing it strictly from beginning to end.
# with open("mynewfile.txt", "r") as f:
#     # 10 character se spaces included:
#     f.seek(10)

#     # tell functions will tell you k hamne kitny numbers p seek kia hai:
#     f.tell()
#     # 5 char read krene hain:
#     data = f.read(5)
#     print(data)


# # truncate() is used when you want to add limited characters like you truncate(5) u r only allowed to keep 5 chars in it


# with open("truncate.txt", "w") as f:
#     f.write("hello my name yasra")
#     f.truncate(7)


with open("file.txt", "rb") as f:
    f.seek(2, 1)
    data = f.read()
    print(data)
