"""Define the Hand class."""


from rules import ranks, suits, hand_values


class Hand:
    """Class for final poker hand.

    Args:
        - cards: list
            List of strings (length=2) representing each card.
    """

    def __init__(self, cards: list):
        """Initiate the class"""
        self.cards = cards

    # Run the following trees to test hand strength
    def determine_value(self) -> str:
        """Return poker hand value"""
        pass

    # Testing tree 1
    def test_straightflush(self) -> (bool, str):
        """Return bool of if straight flush and lead card"""
        pass

    def test_flush(self) -> bool:
        """Return bool of if flush"""
        pass

    def test_straight(self) -> (bool, str):
        """Return bool of if straight and lead card"""
        pass

    # Tree 2
    def test_fourofakind(self) -> bool:
        """Return bool of if four of a kind"""
        pass

    def test_fullhouse(self) -> bool:
        """Return bool of if full house"""
        pass

    def test_threeofakind(self) -> bool:
        """Return bool of if three of a kind"""
        pass

    def test_pair(self) -> bool:
        """Return bool of if pair"""
        pass

    def test_twopairs(self) -> bool:
        """Return bool of if two pairs"""
        pass

    # Underlying methods for gathering info on cards
