from rank import Rank, ranks
from suit import Suit, suits
from card import Card

values = ('Highcard', 'Pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 
            'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')

class Hand:

    def __init__(self, cards):
        self.cards = cards
        if not(self.validate_hand()):
            raise ValueError('Invalid hand input')
        self.cards.sort(reverse = True)
        self.value = self.determine_value()

    def validate_hand(self):
        if type(self.cards) != list:
            return False
        for card in self.cards:
            if not(isinstance(card, Card)):
                return False
        num_cards = len(self.cards)
        for index in range(num_cards - 1):
            if self.cards[index] in self.cards[index + 1: num_cards]:
                return False
        return True
    
    def __repr__(self):
        return str(self.cards)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.value != other.value:
                return False

            if self.value == 'Royal flush':
                return True

            if self.value == 'Straight flush':
                return self.sf_lead == other.sf_lead

            if self.value == 'Four of a kind':
                if self.fours[0] == other.fours[0]:
                    A_highcards = []
                    for card in self.cards:
                        if card.rank != self.fours[0]:
                            A_highcards.append(card.rank)
                    B_highcards =[]
                    for card in other.cards:
                        if card.rank != other.fours[0]:
                            B_highcards.append(card.rank)
                    if A_highcards[0] == B_highcards[0]:
                        return True
                return False

            if self.value == 'Full house':
                if self.threes[0] == other.threes[0]:
                    if len(self.threes) == 2:
                        A_fullof = self.threes[1]
                    else:
                        A_fullof = self.pairs[0]
                    if len(other.threes) == 2:
                        B_fullof = other.threes[1]
                    else:
                        B_fullof = other.pairs[0]
                    if A_fullof == B_fullof:
                        return True
                return False

            if self.value == 'Flush':
                for index in range(5):
                    if self.flush_ranks[index] != other.flush_ranks[index]:
                        return False
                return True

            if self.value == 'Straight':
                return self.straight_lead == other.straight_lead

            if self.value == 'Three of a kind':
                if self.threes[0] == other.threes[0]:
                    A_highcards = []
                    for card in self.cards:
                        if card.rank != self.threes[0]:
                            A_highcards.append(card.rank)
                    B_highcards =[]
                    for card in other.cards:
                        if card.rank != other.threes[0]:
                            B_highcards.append(card.rank)
                    for index in range(2):
                        if A_highcards[index] != B_highcards[index]:
                            return False
                    return True
                return False

            if self.value == 'Two pairs':
                if self.pairs[0] == other.pairs[0] and self.pairs[1] == other.pairs[1]:
                    A_highcards = []
                    for card in self.cards:
                        if card.rank != self.pairs[0] and card.rank != self.pairs[1]:
                            A_highcards.append(card.rank)
                    B_highcards =[]
                    for card in other.cards:
                        if card.rank != other.pairs[0] and card.rank != other.pairs[1]:
                            B_highcards.append(card.rank)
                    if A_highcards[0] == B_highcards[0]:
                        return True
                return False

            if self.value == 'Pair':
                if self.pairs[0] == other.pairs[0]:
                    A_highcards = []
                    for card in self.cards:
                        if card.rank != self.pairs[0]:
                            A_highcards.append(card.rank)
                    B_highcards =[]
                    for card in other.cards:
                        if card.rank != other.pairs[0]:
                            B_highcards.append(card.rank)
                    for index in range(3):
                        if A_highcards[index] != B_highcards[index]:
                            return False
                    return True
                return False

            if self.value == 'Highcard':
                for index in range(5):
                    if self.cards[index].rank != other.cards[index].rank:
                        return False
                return True
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return result        
        if result:
            return False
        if self.value != other.value:
            return values.index(self.value) < values.index(other.value)

        if self.value == 'Straight flush':
            return self.sf_lead < other.sf_lead

        if self.value == 'Four of a kind':
            if self.fours[0] != other.fours[0]:
                return self.fours[0] < other.fours[0]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.fours[0]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.fours[0]:
                    B_highcards.append(card.rank)
            return A_highcards[0] < B_highcards[0]

        if self.value == 'Full house':
            if self.threes[0] != other.threes[0]:
                return self.threes[0] < other.threes[0]
            if len(self.threes) == 2:
                A_fullof = self.threes[1]
            else:
                A_fullof = self.pairs[0]
            if len(other.threes) == 2:
                B_fullof = other.threes[1]
            else:
                B_fullof = other.pairs[0]
            return A_fullof < B_fullof

        if self.value == 'Flush':
            for index in range(5):
                if self.flush_ranks[index] != other.flush_ranks[index]:
                    return self.flush_ranks[index] < other.flush_ranks[index]

        if self.value == 'Straight':
            return self.straight_lead < other.straight_lead

        if self.value == 'Three of a kind':
            if self.threes[0] != other.threes[0]:
                return self.threes[0] < other.threes[0]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.threes[0]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.threes[0]:
                    B_highcards.append(card.rank)
            for index in range(2):
                if A_highcards[index] != B_highcards[index]:
                    return A_highcards[index] < B_highcards[index]

        if self.value == 'Two pairs':
            if self.pairs[0] != other.pairs[0]:
                return self.pairs[0] < other.pairs[0]
            if self.pairs[1] != other.pairs[1]:
                return self.pairs[1] < other.pairs[1]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.pairs[0] and card.rank != self.pairs[1]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.pairs[0] and card.rank != other.pairs[1]:
                    B_highcards.append(card.rank)
            return A_highcards[0] < B_highcards[0]

        if self.value == 'Pair':
            if self.pairs[0] != other.pairs[0]:
                return self.pairs[0] < other.pairs[0]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.pairs[0]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.pairs[0]:
                    B_highcards.append(card.rank)
            for index in range(3):
                if A_highcards[index] != B_highcards[index]:
                    return A_highcards[index] < B_highcards[index]

        if self.value == 'Highcard':
            for index in range(5):
                if self.cards[index].rank != other.cards[index].rank:
                    return self.cards[index].rank < other.cards[index].rank

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return result        
        if result:
            return False
        if self.value != other.value:
            return values.index(self.value) > values.index(other.value)

        if self.value == 'Straight flush':
            return self.sf_lead > other.sf_lead

        if self.value == 'Four of a kind':
            if self.fours[0] != other.fours[0]:
                return self.fours[0] > other.fours[0]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.fours[0]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.fours[0]:
                    B_highcards.append(card.rank)
            return A_highcards[0] > B_highcards[0]

        if self.value == 'Full house':
            if self.threes[0] != other.threes[0]:
                return self.threes[0] > other.threes[0]
            if len(self.threes) == 2:
                A_fullof = self.threes[1]
            else:
                A_fullof = self.pairs[0]
            if len(other.threes) == 2:
                B_fullof = other.threes[1]
            else:
                B_fullof = other.pairs[0]
            return A_fullof > B_fullof

        if self.value == 'Flush':
            for index in range(5):
                if self.flush_ranks[index] != other.flush_ranks[index]:
                    return self.flush_ranks[index] > other.flush_ranks[index]

        if self.value == 'Straight':
            return self.straight_lead > other.straight_lead

        if self.value == 'Three of a kind':
            if self.threes[0] != other.threes[0]:
                return self.threes[0] > other.threes[0]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.threes[0]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.threes[0]:
                    B_highcards.append(card.rank)
            for index in range(2):
                if A_highcards[index] != B_highcards[index]:
                    return A_highcards[index] > B_highcards[index]

        if self.value == 'Two pairs':
            if self.pairs[0] != other.pairs[0]:
                return self.pairs[0] > other.pairs[0]
            if self.pairs[1] != other.pairs[1]:
                return self.pairs[1] > other.pairs[1]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.pairs[0] and card.rank != self.pairs[1]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.pairs[0] and card.rank != other.pairs[1]:
                    B_highcards.append(card.rank)
            return A_highcards[0] > B_highcards[0]

        if self.value == 'Pair':
            if self.pairs[0] != other.pairs[0]:
                return self.pairs[0] > other.pairs[0]
            A_highcards = []
            for card in self.cards:
                if card.rank != self.pairs[0]:
                    A_highcards.append(card.rank)
            B_highcards =[]
            for card in other.cards:
                if card.rank != other.pairs[0]:
                    B_highcards.append(card.rank)
            for index in range(3):
                if A_highcards[index] != B_highcards[index]:
                    return A_highcards[index] > B_highcards[index]

        if self.value == 'Highcard':
            for index in range(5):
                if self.cards[index].rank != other.cards[index].rank:
                    return self.cards[index].rank > other.cards[index].rank
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def determine_value(self):
        sf_test = self.test_straightflush()
        if self.royal:
            return 'Royal flush'
        if sf_test:
            return 'Straight flush'
        if self.test_fourofakind():
            return 'Four of a kind'
        if self.test_fullhouse():
            return 'Full house'
        if self.flush:
            return 'Flush'
        if self.test_straight():
            return 'Straight'
        if self.threeofakind:
            return 'Three of a kind'
        if self.twopairs:
            return 'Two pairs'
        if self.pair:
            return 'Pair'
        return 'Highcard'

    def test_straightflush(self):
        self.royal = False
        if self.test_flush():
            self.flush_ranks = []
            for card in self.cards:
                if card.suit.value == self.flush_suit:
                    self.flush_ranks.append(card.rank)
            if self.flush_ranks[4] == Rank('T'):
                self.royal = True
                return True
            for index in range(len(self.flush_ranks) - 4):
                if ranks.index(self.flush_ranks[index].value) - ranks.index(self.flush_ranks[index + 4].value) == 4:
                    self.sf_lead = self.flush_ranks[index].value
                    return True
            if Rank('A') in self.flush_ranks and self.flush_ranks[len(self.flush_ranks) - 4] == Rank('5'):
                self.sf_lead = '5'
                return True
        return False

    def test_flush(self):
        self.flush = False
        suit_count = self.count_suits()
        for suit in suit_count:
            if suit_count[suit] >= 5:
                self.flush = True
                self.flush_suit = suit
                return True
        return False
    
    def count_suits(self):
        suit_count = {}
        for suit in suits:
            suit_count[suit] = 0
        for card in self.cards:
            suit_count[card.suit.value] += 1
        return suit_count

    def test_straight(self):
        card_ranks_set = self.rank_cards_set()
        for index in range(len(card_ranks_set) - 4):
            if ranks.index(card_ranks_set[index].value) - ranks.index(card_ranks_set[index + 4].value) == 4:
                self.straight = True
                self.straight_lead = card_ranks_set[index].value
                return True
        if Rank('A') in card_ranks_set and card_ranks_set[len(card_ranks_set) - 4] == Rank('5'):
            self.straight = True
            self.straight_lead = '5'
            return True
        return False

    def rank_cards_set(self):
        card_ranks_set = []
        for card in self.cards:
            if card.rank not in card_ranks_set:
                card_ranks_set.append(card.rank)
        return card_ranks_set
    
    def test_fourofakind(self):
        if self.test_threeofakind():
            self.fours = []
            for rank in self.rank_count:
                if self.rank_count[rank] >= 4:
                    self.fours.append(Rank(rank))
            if len(self.fours) >= 1:
                return True
        return False
    
    def test_fullhouse(self):
        if self.test_twopairs():
            if self.threeofakind:
                return True
        return False
    
    def test_threeofakind(self):
        self.threeofakind = False
        if self.test_pair():
            self.threes = []
            for rank in self.rank_count:
                if self.rank_count[rank] >= 3:
                    self.threes.append(Rank(rank))
            if len(self.threes) >= 1:
                self.threeofakind = True
                return True
        return False
    
    def test_twopairs(self):
        self.twopairs = False
        if self.pair:
            if len(self.pairs) >= 2:
                self.twopairs = True
                return True
        return False
    
    def test_pair(self):
        self.pair = False
        self.rank_count = self.count_ranks()
        self.pairs = []
        for rank in self.rank_count:
            if self.rank_count[rank] >= 2:
                self.pairs.append(Rank(rank))
        if len(self.pairs) >= 1:
            self.pair = True
            return True
        return False

    def count_ranks(self):
        rank_count = {}
        for rank in ranks:
            rank_count[rank] = 0
        for card in self.cards:
            rank_count[card.rank.value] += 1
        return rank_count