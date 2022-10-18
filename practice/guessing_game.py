# 3 changes to guess a number
# if user inputs 9 he wins
import random

number = random.randrange(0,9) # this will randomize a number
# number = 5
i = 1
while i <= 9:

    guess = input("Guess" + str(i) +": " )
    if int(guess) != number:
        print("... try again")
    else:
        print("Well done good guess. The number was indeed " + guess)
        break

    print("*" * i)

    i += 1

# print("Game over")

# for num in range(1,9):
#   print("*" * 4)