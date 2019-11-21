# ------------------------------
#   Manages the Hand class
# ------------------------------

# import hand values, etc.
from rules import hand_values_data
from card import Card
from rank import ranks, empty_rank_count
from suit import suits, empty_suit_count
import copy

# create and specify the class
class Hand:
    def __init__(self, cards):
        self.cards = cards
        if not (self.validate_hand()):
            raise ValueError("ERROR: Invalid hand input.")

        self.cards.sort(reverse=True)

        self.suit_count = self.count_suits(self.cards)
        self.rank_count = self.count_ranks(self.cards)

    def validate_hand(self):
        return not any(not (isinstance(card, Card)) for card in self.cards)

    def __repr__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        if not (self.validate_hand()):
            raise ValueError("ERROR: Invalid card added.")

        self.cards.sort(reverse=True)

        self.suit_count[card.suit] += 1
        self.rank_count[card.rank] += 1

    # overwriting comparison methods
    def __eq__(self, other):
        if not (isinstance(other, self.__class__)):
            return NotImplemented

        if self.value != other.value:
            return False

        if self.value == "Royal flush":
            return True

        if self.value == "Straight flush":
            return self.sf_lead == other.sf_lead

        if self.value == "Four of a kind":
            if self.quads[0] == other.quads[0]:

                def gen_qu_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.quads[0]:
                            yield card.rank

                s_hr = list(gen_qu_highranks(self))
                o_hr = list(gen_qu_highranks(other))

                return s_hr[0] == o_hr[0]

            return False

        if self.value == "Full house":
            if self.trips[0] == other.trips[0]:

                def get_fullof(given_object):
                    if len(given_object.trips) == 2:
                        return given_object.trips[1]
                    return given_object.pairs[0]

                s_fullof = get_fullof(self)
                o_fullof = get_fullof(other)

                return s_fullof == o_fullof

            return False

        if self.value == "Flush":
            for index in range(5):
                if self.fcards[index].rank != other.fcards[index].rank:
                    return False

            return True

        if self.value == "Straight":
            return self.straight_lead == other.straight_lead

        if self.value == "Three of a kind":
            if self.trips[0] == other.trips[0]:

                def gen_tr_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.trips[0]:
                            yield card.rank

                s_hr = list(gen_tr_highranks(self))
                o_hr = list(gen_tr_highranks(other))

                for index in range(2):
                    if s_hr[index] != o_hr[index]:
                        return False

                return True

            return False

        if self.value == "Two pairs":
            if self.pairs[0] == other.pairs[0] and self.pairs[1] == other.pairs[1]:

                def gen_tw_highranks(given_object):
                    for card in given_object.cards:
                        if (
                            card.rank != given_object.pairs[0]
                            and card.rank != given_object.pairs[1]
                        ):
                            yield card.rank

                s_hr = list(gen_tw_highranks(self))
                o_hr = list(gen_tw_highranks(other))

                return s_hr[0] == o_hr[0]

            return False

        if self.value == "Pair":
            if self.pairs[0] == other.pairs[0]:

                def gen_pa_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.pairs[0]:
                            yield card.rank

                s_hr = list(gen_pa_highranks(self))
                o_hr = list(gen_pa_highranks(other))

                for index in range(3):
                    if s_hr[index] != o_hr[index]:
                        return False

                return True

            return False

        if self.value == "Highcard":
            for index in range(5):
                if self.cards[index].rank != other.cards[index].rank:
                    return False

            return True

    def __ne__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if not (isinstance(other, self.__class__)):
            return NotImplemented

        # listed in descending order hence reversed comparison
        if self.value != other.value:
            return hand_values_data.index(self.value) > hand_values_data.index(
                other.value
            )

        if self.value == "Royal flush":
            return False

        if self.value == "Straight flush":
            return self.sf_lead < other.sf_lead

        if self.value == "Four of a kind":
            if self.quads[0] == other.quads[0]:

                def gen_qu_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.quads[0]:
                            yield card.rank

                s_hr = list(gen_qu_highranks(self))
                o_hr = list(gen_qu_highranks(other))

                return s_hr[0] < o_hr[0]

            return self.quads[0] < other.quads[0]

        if self.value == "Full house":
            if self.trips[0] == other.trips[0]:

                def get_fullof(given_object):
                    if len(given_object.trips) == 2:
                        return given_object.trips[1]
                    return given_object.pairs[0]

                s_fullof = get_fullof(self)
                o_fullof = get_fullof(other)

                return s_fullof < o_fullof

            return self.trips[0] < other.trips[0]

        if self.value == "Flush":
            for index in range(5):
                if self.fcards[index].rank != other.fcards[index].rank:
                    return self.fcards[index].rank < other.fcards[index].rank

            return False

        if self.value == "Straight":
            return self.straight_lead < other.straight_lead

        if self.value == "Three of a kind":
            if self.trips[0] == other.trips[0]:

                def gen_tr_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.trips[0]:
                            yield card.rank

                s_hr = list(gen_tr_highranks(self))
                o_hr = list(gen_tr_highranks(other))

                for index in range(2):
                    if s_hr[index] != o_hr[index]:
                        return s_hr[index] < o_hr[index]

                return False

            return self.trips[0] < other.trips[0]

        if self.value == "Two pairs":
            if self.pairs[0] == other.pairs[0]:
                if self.pairs[1] == other.pairs[1]:

                    def gen_tw_highranks(given_object):
                        for card in given_object.cards:
                            if (
                                card.rank != given_object.pairs[0]
                                and card.rank != given_object.pairs[1]
                            ):
                                yield card.rank

                    s_hr = list(gen_tw_highranks(self))
                    o_hr = list(gen_tw_highranks(other))

                    return s_hr[0] < o_hr[0]

                return self.pairs[1] < other.pairs[1]

            return self.pairs[0] < other.pairs[0]

        if self.value == "Pair":
            if self.pairs[0] == other.pairs[0]:

                def gen_pa_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.pairs[0]:
                            yield card.rank

                s_hr = list(gen_pa_highranks(self))
                o_hr = list(gen_pa_highranks(other))

                for index in range(3):
                    if s_hr[index] != o_hr[index]:
                        return s_hr[index] < o_hr[index]

                return False

            return self.pairs[0] < other.pairs[0]

        if self.value == "Highcard":
            for index in range(5):
                if self.cards[index].rank != other.cards[index].rank:
                    return self.cards[index].rank < other.cards[index].rank

            return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not (isinstance(other, self.__class__)):
            return NotImplemented

        # listed in descending order hence reversed comparison
        if self.value != other.value:
            return hand_values_data.index(self.value) < hand_values_data.index(
                other.value
            )

        if self.value == "Royal flush":
            return False

        if self.value == "Straight flush":
            return self.sf_lead > other.sf_lead

        if self.value == "Four of a kind":
            if self.quads[0] == other.quads[0]:

                def gen_qu_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.quads[0]:
                            yield card.rank

                s_hr = list(gen_qu_highranks(self))
                o_hr = list(gen_qu_highranks(other))

                return s_hr[0] > o_hr[0]

            return self.quads[0] > other.quads[0]

        if self.value == "Full house":
            if self.trips[0] == other.trips[0]:

                def get_fullof(given_object):
                    if len(given_object.trips) == 2:
                        return given_object.trips[1]
                    return given_object.pairs[0]

                s_fullof = get_fullof(self)
                o_fullof = get_fullof(other)

                return s_fullof > o_fullof

            return self.trips[0] > other.trips[0]

        if self.value == "Flush":
            for index in range(5):
                if self.fcards[index].rank != other.fcards[index].rank:
                    return self.fcards[index].rank > other.fcards[index].rank

            return False

        if self.value == "Straight":
            return self.straight_lead > other.straight_lead

        if self.value == "Three of a kind":
            if self.trips[0] == other.trips[0]:

                def gen_tr_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.trips[0]:
                            yield card.rank

                s_hr = list(gen_tr_highranks(self))
                o_hr = list(gen_tr_highranks(other))

                for index in range(2):
                    if s_hr[index] != o_hr[index]:
                        return s_hr[index] > o_hr[index]

                return False

            return self.trips[0] > other.trips[0]

        if self.value == "Two pairs":
            if self.pairs[0] == other.pairs[0]:
                if self.pairs[1] == other.pairs[1]:

                    def gen_tw_highranks(given_object):
                        for card in given_object.cards:
                            if (
                                card.rank != given_object.pairs[0]
                                and card.rank != given_object.pairs[1]
                            ):
                                yield card.rank

                    s_hr = list(gen_tw_highranks(self))
                    o_hr = list(gen_tw_highranks(other))

                    return s_hr[0] > o_hr[0]

                return self.pairs[1] > other.pairs[1]

            return self.pairs[0] > other.pairs[0]

        if self.value == "Pair":
            if self.pairs[0] == other.pairs[0]:

                def gen_pa_highranks(given_object):
                    for card in given_object.cards:
                        if card.rank != given_object.pairs[0]:
                            yield card.rank

                s_hr = list(gen_pa_highranks(self))
                o_hr = list(gen_pa_highranks(other))

                for index in range(3):
                    if s_hr[index] != o_hr[index]:
                        return s_hr[index] > o_hr[index]

                return False

            return self.pairs[0] > other.pairs[0]

        if self.value == "Highcard":
            for index in range(5):
                if self.cards[index].rank != other.cards[index].rank:
                    return self.cards[index].rank > other.cards[index].rank

            return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    # finds the hand value using tests
    def determine_value(self):
        (sf_bool, sf_lead) = self.test_straightflush()
        if sf_bool:
            self.sf_lead = sf_lead
            if self.sf_lead == ranks[0]:
                self.value = "Royal flush"
                return
            self.value = "Straight flush"
            return

        if self.test_fourofakind():
            self.value = "Four of a kind"
            return

        if self.test_fullhouse():
            self.value = "Full house"
            return

        if self.flush:
            self.value = "Flush"
            return

        (straight_bool, straight_lead) = self.test_straight(self.cards)
        if straight_bool:
            self.straight_lead = straight_lead
            self.value = "Straight"
            return

        if self.threeofakind:
            self.value = "Three of a kind"
            return

        if self.test_twopairs():
            self.value = "Two pairs"
            return

        if self.pair:
            self.value = "Pair"
            return

        self.value = "Highcard"
        return

    # low level tests for analysing hand; sub-trees to show testing order
    # tree 1
    def test_straightflush(self):
        (self.flush, flush_suit) = self.test_flush()

        if self.flush:

            def gen_fcards(fs, cards):
                for card in cards:
                    if card.suit == fs:
                        yield card

            self.fcards = list(gen_fcards(flush_suit, self.cards))
            return self.test_straight(self.fcards)

        return False, None

    def test_flush(self):
        def gen_flush_suits(s_count):
            for s in s_count:
                if s_count[s] >= 5:
                    yield s

        flush_suits = list(gen_flush_suits(self.suit_count))

        if len(flush_suits) == 1:
            return True, flush_suits[0]

        if len(flush_suits) > 1:
            raise ValueError("ERROR: More than one flush not implemented.")

        return False, None

    def test_straight(self, cards):
        distinct_ranks = self.find_distinct_ranks(cards)

        num_dis_ranks = len(distinct_ranks)
        for index in range(num_dis_ranks - 4):
            if distinct_ranks[index] - distinct_ranks[index + 4] == 4:
                return True, distinct_ranks[index]

        # checking for the 5-A straight since A is only high in code
        if ranks[0] in distinct_ranks and distinct_ranks[num_dis_ranks - 4] == ranks[9]:
            return True, ranks[9]

        return False, None

    # tree 2
    def test_fourofakind(self):
        self.quads = list(self.gen_n_counts(self.rank_count, 4))

        if len(self.quads) >= 1:
            return True

        return False

    def test_fullhouse(self):
        self.threeofakind = self.test_threeofakind()
        self.pair = self.test_pair()

        if self.threeofakind and self.pair:
            return True

        elif len(self.trips) == 2:
            return True

        return False

    def test_threeofakind(self):
        self.trips = list(self.gen_n_counts(self.rank_count, 3))

        if len(self.trips) >= 1:
            return True

        return False

    def test_pair(self):
        self.pairs = list(self.gen_n_counts(self.rank_count, 2))

        if len(self.pairs) >= 1:
            return True

        return False

    def test_twopairs(self):
        if len(self.pairs) >= 2:
            return True

        return False

    # basic methods for gathering stats
    def count_suits(self, cards):
        suit_count = copy.copy(empty_suit_count)

        for card in cards:
            suit_count[card.suit] += 1

        return suit_count

    def count_ranks(self, cards):
        rank_count = copy.copy(empty_rank_count)

        for card in cards:
            rank_count[card.rank] += 1

        return rank_count

    def find_distinct_ranks(self, cards):
        def gen_dis_ranks(r_count):
            for r in r_count:
                if r_count[r] >= 1:
                    yield r

        return list(gen_dis_ranks(self.count_ranks(cards)))

    def gen_n_counts(self, r_count, n):
        for r in r_count:
            if r_count[r] == n:
                yield r
