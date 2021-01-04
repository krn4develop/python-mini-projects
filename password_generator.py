import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()?"
print("\t\t\t\t\t********PASSWORD GENERATOR*******")
length = int(input("Enter the length of password you want to generate: "))
password = "".join(random.sample(s, length))
print("The password generated is {}".format(password))
