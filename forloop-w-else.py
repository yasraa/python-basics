# we can use else with a for loop to specify a block of code that will be executed if the loop completes without encountering a break statement. The else block will be executed after the loop finishes iterating over all items in the sequence.

for i in range(6):
    if i == 4:
        break
else:
    print("Loop completed without break")
# In this example, the loop will break when i is equal to 4, so the else block will not be executed. If we change the condition to break at a different value, the else block will be executed if the loop completes without breaking.
