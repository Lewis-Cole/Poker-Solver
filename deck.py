from card import Card
import random

class Deck:

    def __init__(self, card_ranks, card_suits):
        self.card_ranks = card_ranks
        self.card_suits = card_suits
        self.fullcards = list(Deck.make_deck(self))
        self.cards = []
        for card in self.fullcards:
            self.cards.append(card)

    def make_deck(self):
        for rank in self.card_ranks:
            for suit in self.card_suits:
                yield Card(rank, suit)
    
    def remove_dead_cards(self, dead_cards):
        cards_in_deck = []
        for card1 in dead_cards:
            card_in_deck = [card2 for card2 in self.fullcards if card1.rank == card2.rank and card1.suit == card2.suit]
            cards_in_deck.append(card_in_deck[0])
        for card in cards_in_deck:
            self.cards.remove(card)
    
    def get_cards(self, number):
        random.shuffle(self.cards)
        for index in range(number):
            yield self.cards[index]