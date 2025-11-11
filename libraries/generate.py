# import random
# print(random.choice(["heads", "tails"]))
# from random import choice
# print(choice(["heads", "tails"]))
import random

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
