# ------------------------------------
#   Manages the Holding Range class
# ------------------------------------

# import Holding class
from holding import Holding

# create and specify the class
class Holding_Range:

    def __init__(self, holdings):
        self.holdings = holdings
        if not(self.validate_range()):
            raise ValueError('ERROR: Invalid range input.')

    def validate_range(self):
        return all(isinstance(holding, Holding) for holding in self.holdings)
    
    def __repr__(self):
        return str(self.holdings)