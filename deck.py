'''Create and manage the deck and cards.
'''

import random

#define features of a card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

#set types of cards in play
card_rankings = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
card_suits = ('c', 'd', 'h', 's')

#generate deck from specifications
def make_deck():
    for r in card_rankings:
        for s in card_suits:
            yield r + s

full_deck = list(make_deck())

#draw a certain number of cards from deck
def get_card(deck, count):
    random.shuffle(deck)
    for i in range(count):
        yield deck[i]

