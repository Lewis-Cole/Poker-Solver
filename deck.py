# ------------------------------
#   Manages the Deck class
# ------------------------------

# import ranks, suits, the Card class and the random module
from rank import ranks
from suit import suits
from card import Card
import random

# create and specify the class
class Deck:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self.full = list(self.make_deck())
        self.replenish()

    def __repr__(self):
        return str(self.cards)

    def make_deck(self):
        for rank in self.ranks:
            for suit in self.suits:
                yield Card(rank, suit)

    def replenish(self):
        def copy_list(given_list):
            for item in given_list:
                yield item

        self.cards = list(copy_list(self.full))

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, number):
        remaining_cards = len(self.cards)
        if number > remaining_cards:
            raise ValueError(
                "There are only {} cards left in the deck".format(remaining_cards)
            )

        def yield_cards(num):
            for index in range(num):
                yield self.cards[index]

        return list(yield_cards(number))

    def remove(self, cards):
        for card in cards:
            if card in self.cards:
                self.cards.remove(card)


# apply class to ranks and suits
deck = Deck(ranks, suits)
