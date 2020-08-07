age = int(input("Please type your age :"))
name = input("Please type your name :")

if 18 < age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    print("I'm sorry {}, you're not allowed to enter".format(name))