class HRange:

    def __init__(self, holdings):
        self.holdings = holdings
        if not(self.validate_hrange()):
            raise ValueError('Invalid range input')
    
    def validate_hrange(self):
        if type(self.holdings) != list:
            return False

        return True