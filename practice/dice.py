import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        # return a tuple
        return first, second


calls = Dice()
print(calls.roll())
