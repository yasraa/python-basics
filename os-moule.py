import os

# # we can use os module to get the current working directory
# print(os.getcwd())

# # we can also list all the files and directories in the current working directory
# print(os.listdir())

# os.rmdir(new_directory)


main_folder = "main_folder"
sub_folder = ["assignments", "exercises", "projects"]
try:
    for folders in sub_folder:
        path = os.path.join(main_folder, folders)

        os.makedirs(path, exist_ok=True)
    print(f"Successfully created '{main_folder}' with 3 inner folders!")
except Exception as e:
    print(e)
