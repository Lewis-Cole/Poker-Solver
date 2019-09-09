from hand import Hand

class HRange:

    def __init__(self, hands):
        self.hands = hands
        if not(self.validate_hrange()):
            raise ValueError('Invalid range input')
    
    def validate_hrange(self):
        if type(self.hands) != list:
            return False
        for hand in self.hands:
            if not(isinstance(hand, Hand)):
                return False
        return True