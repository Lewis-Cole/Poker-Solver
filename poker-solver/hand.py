"""Define the Hand class."""


from .rules import ranks, suits, hand_values


class Hand:
    """Class for poker hand of up to 7 cards.

    Args:
        - cards: list
            List of strings (length=2) representing each card.
    """

    def __init__(self, cards: list):
        """Initiate the class"""
        self.cards = cards
        self.value = self.determine_value()

    # hand comparison functions eq, ne, lt, le, gt, ge
    def __eq__(self, other):
        """Returns bool of if two poker hands have equal strength"""
        # check if they have the same hand value
        if self.value != other.value:
            return False

        # each hand value with unique test for each
        # Royal flush
        if self.value == hand_values[9]:
            return True

        # Straight flush
        if self.value == hand_values[8]:
            return self.sf_lead == other.sf_lead

        # Four of a kind
        if self.value == hand_values[7]:
            if self.quads[0] == other.quads:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 4
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 4
                ]
                return self_highranks[-1] == other_highranks[-1]
            return False

        # Full house
        if self.value == hand_values[6]:
            if self.trips[-1] == other.trips[-1]:
                self_pair = self.trips[-2] if len(self.trips) == 2 else self.pairs[-1]
                other_pair = (
                    other.trips[-2] if len(other.trips) == 2 else other.pairs[-1]
                )
                return self_pair == other_pair
            return False

        # Flush
        if self.value == hand_values[5]:
            self_flushranks = [card[0] for card in self.flush_cards]
            self_flushranks = [rank for rank in ranks if rank in self_flushranks]
            other_flushranks = [card[0] for card in other.flush_cards]
            other_flushranks = [rank for rank in ranks if rank in other_flushranks]
            for index in range(5):
                if self_flushranks[-(index + 1)] != other_flushranks[-(index + 1)]:
                    return False
            return True

        # Straight
        if self.value == hand_values[4]:
            return self.straight_lead == other.straight_lead

        # Three of a kind
        if self.value == hand_values[3]:
            if self.trips[-1] == other.trips[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 3
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 3
                ]
                for index in range(2):
                    if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                        return False
                return True
            return False

        # Two pairs
        if self.value == hand_values[2]:
            if self.pairs[-1] == other.pairs[-1]:
                if self.pairs[-2] == other.pairs[-2]:
                    self_highranks = [
                        rank
                        for rank in self.rank_dict
                        if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 2
                    ]
                    other_highranks = [
                        rank
                        for rank in other.rank_dict
                        if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 2
                    ]
                    return self_highranks[-1] == other_highranks[-1]
                return False
            return False

        # Pair
        if self.value == hand_values[1]:
            if self.pairs[-1] == other.pairs[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 2
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 2
                ]
                for index in range(3):
                    if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                        return False
                return True
            return False

        # Highcard
        if self.value == hand_values[0]:
            self_highranks = [
                rank for rank in self.rank_dict if self.rank_dict[rank] >= 1
            ]
            other_highranks = [
                rank for rank in other.rank_dict if other.rank_dict[rank] >= 1
            ]
            for index in range(5):
                if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                    return False
            return True

    def __ne__(self, other):
        """Returns bool of if two poker hands do not have equal strength"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Returns bool of if self strength less than other strength"""
        # check if they have the same hand value
        if self.value != other.value:
            return hand_values.index(self.value) < hand_values.index(other.value)

        # each hand value with unique test for each
        # Royal flush
        if self.value == hand_values[9]:
            return False

        # Straight flush
        if self.value == hand_values[8]:
            return ranks.index(self.sf_lead) < ranks.index(other.sf_lead)

        # Four of a kind
        if self.value == hand_values[7]:
            if self.quads[-1] == other.quads[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 4
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 4
                ]
                return ranks.index(self_highranks[-1]) < ranks.index(
                    other_highranks[-1]
                )
            return ranks.index(self.quads[-1]) < ranks.index(other.quads[-1])

        # Full house
        if self.value == hand_values[6]:
            if self.trips[-1] == other.trips[-1]:
                self_pair = self.trips[-2] if len(self.trips) == 2 else self.pairs[-1]
                other_pair = (
                    other.trips[-2] if len(other.trips) == 2 else other.pairs[-1]
                )
                return ranks.index(self_pair) < ranks.index(other_pair)
            return ranks.index(self.trips[-1]) < ranks.index(other.trips[-1])

        # Flush
        if self.value == hand_values[5]:
            self_flushranks = [card[0] for card in self.flush_cards]
            self_flushranks = [rank for rank in ranks if rank in self_flushranks]
            other_flushranks = [card[0] for card in other.flush_cards]
            other_flushranks = [rank for rank in ranks if rank in other_flushranks]
            for index in range(5):
                if self_flushranks[-(index + 1)] != other_flushranks[-(index + 1)]:
                    return ranks.index(self_flushranks[-(index + 1)]) < ranks.index(
                        other_flushranks[-(index + 1)]
                    )
            return False

        # Straight
        if self.value == hand_values[4]:
            return ranks.index(self.straight_lead) < ranks.index(other.straight_lead)

        # Three of a kind
        if self.value == hand_values[3]:
            if self.trips[-1] == other.trips[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 3
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 3
                ]
                for index in range(2):
                    if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                        return ranks.index(self_highranks[-(index + 1)]) < ranks.index(
                            other_highranks[-(index + 1)]
                        )
                return False
            return ranks.index(self.trips[-1]) < ranks.index(other.trips[-1])

        # Two pairs
        if self.value == hand_values[2]:
            if self.pairs[-1] == other.pairs[-1]:
                if self.pairs[-2] == other.pairs[-2]:
                    self_highranks = [
                        rank
                        for rank in self.rank_dict
                        if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 2
                    ]
                    other_highranks = [
                        rank
                        for rank in other.rank_dict
                        if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 2
                    ]
                    return ranks.index(self_highranks[-1]) < ranks.index(
                        other_highranks[-1]
                    )
                return ranks.index(self.pairs[-2]) < ranks.index(other.pairs[-2])
            return ranks.index(self.pairs[-1]) < ranks.index(other.pairs[-1])

        # Pair
        if self.value == hand_values[1]:
            if self.pairs[-1] == other.pairs[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 2
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 2
                ]
                for index in range(3):
                    if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                        return ranks.index(self_highranks[-(index + 1)]) < ranks.index(
                            other_highranks[-(index + 1)]
                        )
                return False
            return ranks.index(self.pairs[-1]) < ranks.index(other.pairs[-1])

        # Highcard
        if self.value == hand_values[0]:
            self_highranks = [
                rank for rank in self.rank_dict if self.rank_dict[rank] >= 1
            ]
            other_highranks = [
                rank for rank in other.rank_dict if other.rank_dict[rank] >= 1
            ]
            for index in range(5):
                if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                    return ranks.index(self_highranks[-(index + 1)]) < ranks.index(
                        other_highranks[-(index + 1)]
                    )
            return False

    def __le__(self, other):
        """Returns bool self less or equal other"""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Returns bool self greater than other"""
        # check if they have the same hand value
        if self.value != other.value:
            return hand_values.index(self.value) > hand_values.index(other.value)

        # each hand value with unique test for each
        # Royal flush
        if self.value == hand_values[9]:
            return False

        # Straight flush
        if self.value == hand_values[8]:
            return ranks.index(self.sf_lead) > ranks.index(other.sf_lead)

        # Four of a kind
        if self.value == hand_values[7]:
            if self.quads[-1] == other.quads[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 4
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 4
                ]
                return ranks.index(self_highranks[-1]) > ranks.index(
                    other_highranks[-1]
                )
            return ranks.index(self.quads[-1]) > ranks.index(other.quads[-1])

        # Full house
        if self.value == hand_values[6]:
            if self.trips[-1] == other.trips[-1]:
                self_pair = self.trips[-2] if len(self.trips) == 2 else self.pairs[-1]
                other_pair = (
                    other.trips[-2] if len(other.trips) == 2 else other.pairs[-1]
                )
                return ranks.index(self_pair) > ranks.index(other_pair)
            return ranks.index(self.trips[-1]) > ranks.index(other.trips[-1])

        # Flush
        if self.value == hand_values[5]:
            self_flushranks = [card[0] for card in self.flush_cards]
            self_flushranks = [rank for rank in ranks if rank in self_flushranks]
            other_flushranks = [card[0] for card in other.flush_cards]
            other_flushranks = [rank for rank in ranks if rank in other_flushranks]
            for index in range(5):
                if self_flushranks[-(index + 1)] != other_flushranks[-(index + 1)]:
                    return ranks.index(self_flushranks[-(index + 1)]) > ranks.index(
                        other_flushranks[-(index + 1)]
                    )
            return False

        # Straight
        if self.value == hand_values[4]:
            return ranks.index(self.straight_lead) > ranks.index(other.straight_lead)

        # Three of a kind
        if self.value == hand_values[3]:
            if self.trips[-1] == other.trips[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 3
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 3
                ]
                for index in range(2):
                    if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                        return ranks.index(self_highranks[-(index + 1)]) > ranks.index(
                            other_highranks[-(index + 1)]
                        )
                return False
            return ranks.index(self.trips[-1]) > ranks.index(other.trips[-1])

        # Two pairs
        if self.value == hand_values[2]:
            if self.pairs[-1] == other.pairs[-1]:
                if self.pairs[-2] == other.pairs[-2]:
                    self_highranks = [
                        rank
                        for rank in self.rank_dict
                        if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 2
                    ]
                    other_highranks = [
                        rank
                        for rank in other.rank_dict
                        if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 2
                    ]
                    return ranks.index(self_highranks[-1]) > ranks.index(
                        other_highranks[-1]
                    )
                return ranks.index(self.pairs[-2]) > ranks.index(other.pairs[-2])
            return ranks.index(self.pairs[-1]) > ranks.index(other.pairs[-1])

        # Pair
        if self.value == hand_values[1]:
            if self.pairs[-1] == other.pairs[-1]:
                self_highranks = [
                    rank
                    for rank in self.rank_dict
                    if self.rank_dict[rank] >= 1 and self.rank_dict[rank] != 2
                ]
                other_highranks = [
                    rank
                    for rank in other.rank_dict
                    if other.rank_dict[rank] >= 1 and other.rank_dict[rank] != 2
                ]
                for index in range(3):
                    if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                        return ranks.index(self_highranks[-(index + 1)]) > ranks.index(
                            other_highranks[-(index + 1)]
                        )
                return False
            return ranks.index(self.pairs[-1]) > ranks.index(other.pairs[-1])

        # Highcard
        if self.value == hand_values[0]:
            self_highranks = [
                rank for rank in self.rank_dict if self.rank_dict[rank] >= 1
            ]
            other_highranks = [
                rank for rank in other.rank_dict if other.rank_dict[rank] >= 1
            ]
            for index in range(5):
                if self_highranks[-(index + 1)] != other_highranks[-(index + 1)]:
                    return ranks.index(self_highranks[-(index + 1)]) > ranks.index(
                        other_highranks[-(index + 1)]
                    )
            return False

    def __ge__(self, other):
        """Returns bool self greater or equal other"""
        return self.__gt__(other) or self.__eq__(other)

    # Run the following trees to test hand strength
    def determine_value(self) -> str:
        """Return poker hand value"""
        self.rank_dict = self.count_ranks()
        self.suit_dict = self.count_suits()

        (sf_bool, self.sf_lead) = self.test_straightflush()
        if sf_bool:
            if self.sf_lead == "A":
                # Royal flush
                return hand_values[9]
            # Straight flush
            return hand_values[8]

        if self.test_fourofakind():
            return hand_values[7]

        if self.test_fullhouse():
            return hand_values[6]

        if self.flush:
            return hand_values[5]

        (straight_bool, self.straight_lead) = self.test_straight(self.cards)
        if straight_bool:
            return hand_values[4]

        if self.threeofakind:
            return hand_values[3]

        if self.test_twopairs():
            return hand_values[2]

        if self.pair:
            return hand_values[1]

        return hand_values[0]

    # Testing tree 1
    def test_straightflush(self) -> (bool, str):
        """Return bool of if straight flush and lead card"""
        (self.flush, flush_suit) = self.test_flush()

        if self.flush:
            self.flush_cards = [card for card in self.cards if card[1] == flush_suit]
            return self.test_straight(self.flush_cards)

        return (False, None)

    def test_flush(self) -> (bool, str):
        """Return bool of if flush and flush suit"""
        flush_suits = [suit for suit in self.suit_dict if self.suit_dict[suit] >= 5]

        if len(flush_suits) >= 1:
            return (True, flush_suits[0])

        return False, None

    def test_straight(self, cards) -> (bool, str):
        """Return bool of if straight and lead card"""
        ranks_in_hand = [card[0] for card in cards]
        straight_ranks = ["A"] + list(ranks)

        count = 0
        made_straight = False
        for rank in straight_ranks:
            if rank in ranks_in_hand:
                last_rank = rank
                count += 1
            else:
                if made_straight == True:
                    return (True, last_rank)
                count = 0
            if count == 5:
                made_straight = True
        if made_straight == True:
            return (True, last_rank)

        return (False, None)

    # Tree 2
    def test_fourofakind(self) -> bool:
        """Return bool of if four of a kind"""
        self.quads = [rank for rank in self.rank_dict if self.rank_dict[rank] == 4]
        return len(self.quads) >= 1

    def test_fullhouse(self) -> bool:
        """Return bool of if full house"""
        self.threeofakind = self.test_threeofakind()
        self.pair = self.test_pair()
        return (self.threeofakind and self.pair) or len(self.trips) >= 2

    def test_threeofakind(self) -> bool:
        """Return bool of if three of a kind"""
        self.trips = [rank for rank in self.rank_dict if self.rank_dict[rank] == 3]
        return len(self.trips) >= 1

    def test_pair(self) -> bool:
        """Return bool of if pair"""
        self.pairs = [rank for rank in self.rank_dict if self.rank_dict[rank] == 2]
        return len(self.pairs) >= 1

    def test_twopairs(self) -> bool:
        """Return bool of if two pairs"""
        return len(self.pairs) >= 2

    # Underlying methods for gathering info on cards
    def count_suits(self) -> dict:
        """Return dictionary with key = suit, value = count"""
        suit_dict = {suit: 0 for suit in suits}
        for card in self.cards:
            suit_dict[card[1]] += 1
        return suit_dict

    def count_ranks(self) -> dict:
        """Return dictionary with key = rank, value = count"""
        rank_dict = {rank: 0 for rank in ranks}
        for card in self.cards:
            rank_dict[card[0]] += 1
        return rank_dict
