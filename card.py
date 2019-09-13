# ------------------------------
#   Manages the Card class
# ------------------------------

# import Rank and Suit classes
from rank import Rank
from suit import Suit

# create and specify the class
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if not(self.validate_card()):
            raise ValueError('ERROR: Invalid card input.')

    def validate_card(self):
        return isinstance(self.rank, Rank) and isinstance(self.suit, Suit)
    
    def __repr__(self):
        return self.rank.__repr__() + self.suit.__repr__()
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rank == other.rank and self.suit == other.suit
        return NotImplemented
    
    def __ne__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return result
        return not result
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if self.rank == other.rank:
                return self.suit < other.suit
            return self.rank < other.rank
        return NotImplemented
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if self.rank == other.rank:
                return self.suit > other.suit
            return self.rank > other.rank
        return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


# easy to use function for testing
def createcard(cardstring):
    rank = Rank(cardstring[0])
    suit = Suit(cardstring[1])
    return Card(rank, suit)