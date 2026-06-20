import random

signs = {"snake": 1, "water": 2, "gun": 3}

print(f"options: {list(signs.keys())}")

user_selection = input("select one: ").lower().strip()
comp_selection = random.choice(list(signs))
print(comp_selection)

if user_selection == comp_selection:
    print("draw")

elif user_selection == "snake" and comp_selection == "water":
    print("you win")

elif user_selection == "gun" and comp_selection == "snake":
    print("you win")

elif user_selection == "water" and comp_selection == "gun":
    print("you win")

else:
    print("computer win")
