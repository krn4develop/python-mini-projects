import random
import sys

print("\t\t\t\t\t ********Guessing Game*******")
print("1. Play\n2. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    number = int(input("Guess a number from 1 to 100: "))
    guess = random.randint(1, 100)
    if guess == number:
        print("Perfect! You guessed correct number {}".format(guess))
    else:
        print("Oh no! The correct number was {}.\nTry again next time.".format(guess))
else:
    sys.exit()
