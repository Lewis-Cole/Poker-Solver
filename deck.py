from rank import Rank
from suit import Suit
from card import Card
import random

class Deck:

    def __init__(self, card_ranks, card_suits):
        self.card_ranks = card_ranks
        self.card_suits = card_suits
        self.fullcards = list(self.make_deck())
        self.replenish()
    
    def __repr__(self):
        return str(self.cards)

    def make_deck(self):
        for rank in self.card_ranks:
            for suit in self.card_suits:
                yield Card(Rank(rank), Suit(suit))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, number):
        if number > len(self.cards):
            raise ValueError('There are only ' + str(len(self.cards)) +' cards left in the deck')
        cards = []
        for index in range(number):
            cards.append(self.cards[index])
        return cards

    def remove(self, cards):
        for card in cards:
            if card in self.cards:
                self.cards.remove(card)
    
    def replenish(self):
        self.cards = []
        for card in self.fullcards:
            self.cards.append(card)