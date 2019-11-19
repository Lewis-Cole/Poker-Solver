# ------------------------------
#   Manages the Suit class
# ------------------------------

# import the list of suits from rules
from rules import suits_data

# create and specify the class
class Suit:
    def __init__(self, value):
        self.value = value
        if not (self.validate_suit()):
            raise ValueError("ERROR: Invalid suit input.")

    def validate_suit(self):
        if self.value in suits_data:
            return True
        return False

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

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
            return suits_data.index(self.value) > suits_data.index(other.value)
        return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return suits_data.index(self.value) < suits_data.index(other.value)
        return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


# apply class to data
def data_to_suit(data):
    for value in data:
        yield Suit(value)


suits = list(data_to_suit(suits_data))


# empty suit dictionary
empty_suit_count = {}

for suit in suits:
    empty_suit_count[suit] = 0
