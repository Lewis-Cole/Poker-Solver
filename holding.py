# ------------------------------
#   Manages the Holding class
# ------------------------------

# import Card class
from card import Card

# create and specify the class
class Holding:

    def __init__(self, cards):
        self.cards = cards
        if not(self.validate_holding()):
            raise ValueError('ERROR: Invalid holding input.')

    def validate_holding(self):
        return all(isinstance(card, Card) for card in self.cards)
    
    def __repr__(self):
        return str(self.cards[0]) + str(self.cards[1])