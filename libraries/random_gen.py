# import random
# print(random.choice(["heads", "tails"]))
# from random import choice
# print(choice(["heads", "tails"]))
import random


def choose_a_card(cards):
    return random.choice(cards)


def shuffle_cards(cards):
    return random.shuffle(cards)


def choose_cards(cards, n):
    return random.choices(cards, k=n)


def choose_unique_cards(cards, n):
    return random.sample(cards, k=n)


def choose_cards_with_weigths(cards, n, w):
    return random.choices(cards, weights=w, k=n)


def seed_and_choose(cards, n):
    random.seed(0)
    return random.sample(cards, k=n)


def main():
    number = random.randint(1, 10)
    print(number)

    cards = ["jack", "queen", "king"]
    # print(choose_a_card(cards))
    # print(choose_cards(cards,n=2))
    # print(choose_unique_cards(cards,n=2))
    print(choose_cards_with_weigths(cards, n=2, w=[75, 25, 0]))
    print(seed_and_choose(cards, n=2))


main()
