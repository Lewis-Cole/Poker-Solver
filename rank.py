ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

class Rank:
    def __init__(self, value):
        self.value = value
        if not(self.validate_rank()):
            raise ValueError('Invalid rank input')

    def validate_rank(self):
        if self.value in ranks:
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
            return ranks.index(self.value) < ranks.index(other.value)
        return NotImplemented
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return ranks.index(self.value) > ranks.index(other.value)
        return NotImplemented
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)