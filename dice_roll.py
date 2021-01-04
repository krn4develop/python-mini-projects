import random
import sys

print("\t\t\t\t\t ****************WELCOME TO DICE ROLLER*************")
print("1. Play the game")
print("2. Exit")
choice = int(input("Press the number as per your choice: "))
if choice == 1:
    dice = random.randint(1, 6)
    print("You got {}".format(dice))
else:
    sys.exit()
