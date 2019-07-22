from card import Card, card_ranks, card_suits

class Hand:

    def __init__(self, cards):
        self.cards = cards
        Hand.index_hand(self)
        Hand.index_counts(self)
        if not(Hand.validate_hand(self)):
            raise ValueError('Invalid hand input.')

    def validate_hand(self):
        if type(self.cards) != list:
            return False
        #elif len(self.indices) != len(set(self.indices)):
            #return False
        else:
            for card in self.cards:
                if not(Card.validate_card(card)):
                    return False
            return True
    
    def index_hand(self):
        self.indices = []
        for card in self.cards:
            Card.index_card(card)
            self.indices.append(card.properties)
        self.sorted_indices = sorted(sorted(self.indices, key = lambda list: list[1], reverse = True), key = lambda list: list[0], reverse = True)
        self.ranks = [rank_index for (rank_index, _) in self.sorted_indices]
        self.suits = [suit_index for (_, suit_index) in self.sorted_indices]
    
    def index_counts(self):
        self.rank_counts = []
        self.suit_counts = []
        for _ in card_ranks:
            self.rank_counts.append(0)
        for _ in card_suits:
            self.suit_counts.append(0)
        for (rank_index, suit_index) in self.indices:
            self.rank_counts[rank_index] += 1
            self.suit_counts[suit_index] += 1
        self.rcc = [0, 0, 0, 0, 0]
        for index in self.rank_counts:
            self.rcc[index] += 1
    
    def test_flush(self):
        if any(self.suit_counts[index] >= 5 for index in self.suit_counts):
            return True
        else:
            return False
    
    def test_straight(self):
        self.ranks.append(-1) if card_ranks.index('A') in self.ranks else None
        self.ranks_set = sorted(set(self.ranks), reverse = True)
        if any(self.ranks_set[index] - self.ranks_set[index + 4] == 4 for index in range(len(self.ranks_set) - 4)):
            return True
        else:
            return False
    
    def test_straightflush(self):
        self.royal = False
        for index1 in range(len(self.suit_counts)):
            if self.suit_counts[index1] >= 5:
                flush_ranks = []
                for (rank_index, suit_index) in self.sorted_indices:
                    flush_ranks.append(rank_index) if suit_index == index1 else None
                flush_ranks.append(-1) if card_ranks.index('A') in flush_ranks else None
                flush_ranks_set = sorted(set(flush_ranks), reverse = True)
                self.royal = True if flush_ranks_set[4] == 8 else False
                if any(flush_ranks_set[index2] - flush_ranks_set[index2 + 4] == 4 for index2 in range(len(flush_ranks_set) - 4)):
                    return True
        return False
    
    def test_fourofakind(self):
        if self.rcc[4] >= 1:
            return True
        else:
            return False
    
    def test_fullhouse(self):
        if self.rcc[3] >= 2 or (self.rcc[3] == 1 and self.rcc[2] >= 1):
            return True
        else:
            return False
    
    def test_threeofakind(self):
        if self.rcc[3] >= 1:
            return True
        else:
            return False
    
    def test_twopairs(self):
        if self.rcc[2] >= 2:
            return True
        else:
            return False
    
    def test_pair(self):
        if self.rcc[2] >= 1:
            return True
        else:
            return False
    
    def determine_value(self):
        sf_test = Hand.test_straightflush(self)
        if self.royal:
            self.value = 'Royal Flush'
        elif sf_test:
            self.value = 'Straight Flush'
        elif Hand.test_fourofakind(self):
            self.value = 'Four of a kind'
        elif Hand.test_fullhouse(self):
            self.value = 'Full house'
        elif Hand.test_flush(self):
            self.value = 'Flush'
        elif Hand.test_straight(self):
            self.value = 'Straight'
        elif Hand.test_threeofakind(self):
            self.value = 'Three of a kind'
        elif Hand.test_twopairs(self):
            self.value = 'Two pairs'
        elif Hand.test_pair(self):
            self.value = 'Pair'
        else:
            self.value = 'Highcard'