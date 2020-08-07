import random

highest = 10
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
guess = highest + 1
print("Please guess number between 1 and {}: ".format(highest))

while(guess != answer and guess != 0):
    guess = int(input())
    if guess > answer:
        print("Please guess lower :")
    elif guess < answer:
        print("Please guess higher :")
if guess == answer:
    print("You got a right answer")
elif guess == 0:
    print("game over")

# if guess == answer:
#     print("You got it first time")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print("Please guess higher")