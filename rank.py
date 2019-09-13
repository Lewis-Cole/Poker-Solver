# ------------------------------
#   Manages the Rank class
# ------------------------------

# import the list of ranks from rules
from rules import ranks_data

# create and specify the class
class Rank:

    def __init__(self, value):
        self.value = value
        if not(self.validate_rank()):
            raise ValueError('ERROR: Invalid rank input.')

    def validate_rank(self):
        if self.value in ranks_data:
            return True
        return False
    
    def __repr__(self):
        return self.value
    
    def __hash__(self):
        return hash(self.value)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return ranks_data.index(other.value) - ranks_data.index(self.value)
        return NotImplemented

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
            return ranks_data.index(self.value) > ranks_data.index(other.value)
        return NotImplemented
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return ranks_data.index(self.value) < ranks_data.index(other.value)
        return NotImplemented
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


# apply class to data
def data_to_rank(data):
    for value in data:
        yield Rank(value)

ranks = list(data_to_rank(ranks_data))