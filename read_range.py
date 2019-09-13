# ----------------------------------------------------------------
#   This file contains functions for converting text to ranges
# ----------------------------------------------------------------

# import here
from holding_range import Holding_Range
from holding import Holding
from card import Card
from rank import ranks, Rank
from suit import suits

# function to covert equilab range text into ranges
def read_range(range_text):
    components = range_text.split(',')

    def gen_holding(components):
        for subrange in components:
            for holding in read_subrange(subrange):
                yield holding

    holdings = list(gen_holding(components))

    return Holding_Range(holdings)


def read_subrange(text):
    text_length = len(text)

    # e.g. '44', 'JJ'
    if text_length == 2:
        for combo in get_pairs(Rank(text[0])):
            yield combo
    
    # e.g. '55+' or 'KQs' or 'AJo'
    elif text_length == 3:
        # '55+'
        if text[2] == '+':
            pair_rank = Rank(text[0])
            for rank in ranks:
                if rank >= pair_rank:
                    for combo in get_pairs(rank):
                        yield combo
        
        # 'KQs'
        elif text[2] == 's':
            rank1 = Rank(text[0])
            rank2 = Rank(text[1])
            for combo in get_suited(rank1, rank2):
                yield combo
        
        # 'AJo'
        elif text[2] == 'o':
            rank1 = Rank(text[0])
            rank2 = Rank(text[1])
            for combo in get_offsuit(rank1, rank2):
                yield combo
    
    # 'K4s+' or 'A2o+'
    elif text_length == 4:
        # 'K4s+'
        if text[2] == 's':
            rank1 = Rank(text[0])
            rank2 = Rank(text[1])
            for rank in ranks:
                if rank >= rank2 and rank < rank1:
                    for combo in get_suited(rank1, rank):
                        yield combo

        # 'A2o+'
        if text[2] == 'o':
            rank1 = Rank(text[0])
            rank2 = Rank(text[1])
            for rank in ranks:
                if rank >= rank2 and rank < rank1:
                    for combo in get_offsuit(rank1, rank):
                        yield combo
    
    # '99-22'
    elif text_length == 5:
        rank1 = Rank(text[0])
        rank2 = Rank(text[3])
        for rank in ranks:
            if rank >= rank2 and rank <= rank1:
                for combo in get_pairs(rank):
                    yield combo
    
    # 'A5s-A2s' or 'AQo-A9o'
    elif text_length == 7:
        # 'A5s-A2s'
        if text[2] == 's':
            rank1 = Rank(text[0])
            rank2_up = Rank(text[1])
            rank2_lw = Rank(text[5])
            for rank in ranks:
                if rank >= rank2_lw and rank <= rank2_up:
                    for combo in get_suited(rank1, rank):
                        yield combo

        # 'AQo-A9o'
        if text[2] == 'o':
            rank1 = Rank(text[0])
            rank2_up = Rank(text[1])
            rank2_lw = Rank(text[5])
            for rank in ranks:
                if rank >= rank2_lw and rank <= rank2_up:
                    for combo in get_offsuit(rank1, rank):
                        yield combo

    else:
        return NotImplemented

# turn ranks into combos for holdings
def get_pairs(rank):
    def gen_cards(rank):
        for suit in suits:
            yield Card(rank, suit)
    
    pair_cards = list(gen_cards(rank))

    num_cards = len(pair_cards)
    for index1 in range(num_cards - 1):
        for index2 in range(index1 + 1, num_cards):
            yield Holding([pair_cards[index1], pair_cards[index2]])

def get_suited(rank1, rank2):
    for suit in suits:
        card1 = Card(rank1, suit)
        card2 = Card(rank2, suit)
        yield Holding([card1, card2])

def get_offsuit(rank1, rank2):
    for suit1 in suits:
        for suit2 in suits:
            if suit1 != suit2:
                card1 = Card(rank1, suit1)
                card2 = Card(rank2, suit2)
                yield Holding([card1, card2])
