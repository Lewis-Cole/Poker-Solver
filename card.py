card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
card_suits = ('c', 'd', 'h', 's')

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if not(Card.validate_card(self)):
            raise ValueError('Invalid card input.')
    
    def validate_card(self):
        if len(self.rank) != 1 or len(self.suit) != 1:
            return False
        elif type(self.rank) != str or type(self.suit) != str:
            return False
        elif not(self.rank in card_ranks):
            return False
        elif not(self.suit in card_suits):
            return False
        else:
            return True
    
    def index_card(self):
        self.properties = []
        self.properties.append(card_ranks.index(self.rank))
        self.properties.append(card_suits.index(self.suit))