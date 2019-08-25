suits = ('c', 'd', 'h', 's')

class Suit:
    def __init__(self, value):
        self.value = value
        if not(self.validate_suit()):
            raise ValueError('Invalid suit input')
    
    def validate_suit(self):
        if self.value in suits:
            return True
        return False
    
    def __repr__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return NotImplemented
    
    def __ne__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return suits.index(self.value) < suits.index(other.value)
        return NotImplemented
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return suits.index(self.value) > suits.index(other.value)
        return NotImplemented
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)