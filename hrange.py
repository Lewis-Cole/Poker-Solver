from hand import Hand

class Range:

    def __init__(self, hands):
        self.hands = hands
        if not(self.validate_range()):
            raise ValueError('Invalid range input')
    
    def validate_range(self):
        if type(self.hands) != list:
            return False
        for hand in self.hands:
            if not(isinstance(hand, Hand)):
                return False
        return True