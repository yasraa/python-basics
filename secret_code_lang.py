# Secret Code Language
import random
import string

pool = string.ascii_letters
random_string = "".join(random.choices(pool, k=3))

print(random_string)

code = input("do you wanna encode or decode? : ")
word = input("enter a word: ")

if code == "encode":
    if len(word) < 3:
        print("Word must have at least 3 letters.")
    else:
        modified_text = random_string + word[1:] + word[0] + random_string
        print(modified_text)
elif code == "decode":
    remove_char = word[3:-3]
    decoded_text = remove_char[-1] + remove_char[:-1]
    print(decoded_text)yui
else:    
    print("Invalid option. Please choose 'encode' or 'decode'.")