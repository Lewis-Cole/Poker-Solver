'''Take a set of cards and determine the strongest hand value.
'''

from deck import card_rankings, card_suits, deck, get_card


hand_values = ('Highcard', 'Pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 
                'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')


def determine_hand_value(cards):
    if valid_hand(cards) != 'Valid hand':
        return valid_hand(cards)

    repcardvalue = test_repeatrankhands(cards)
    if test_straightflush(cards) != 'n':
        return test_straightflush(cards)
    elif repcardvalue == 'Four of a kind':
        return repcardvalue
    elif repcardvalue == 'Full house':
        return repcardvalue
    elif test_flush(cards) != 'n':
        return test_flush(cards)
    elif test_straight(cards) != 'n':
        return test_straight(cards)
    else:
        return repcardvalue


def valid_hand(cards):
    if type(cards) != list:
        return ('ERROR - Cards should be given as a list')
    elif any([type(i) != str or len(i) != 2 for i in cards]):
        return ('ERROR - Cards should be strings of length 2')
    elif any([not(j in deck) for j in cards]):
        return ('ERROR - Cards not from specified deck')
    elif len(cards) != len(set(cards)):
        return ('ERROR - Duplicate cards')
    else:
        return ('Valid hand')


def test_straightflush(cards):
    result = 'n'
    if test_flush(cards) == 'Flush':
        suit_count = count_suits(cards)
        for i in suit_count:
            if suit_count[i] >= 5:
                flush_cards = []
                for j in cards:
                    flush_cards.append(j) if j[1] == i else None
                if test_straight(flush_cards) == 'Straight':
                    result = 'Straight flush'
                    flush_ranks = card_to_rank(flush_cards)
                    sflush_ranks = sorted(flush_ranks, reverse = True)
                    if sflush_ranks[4] == 10:   #if member 4 is 10 then only higher cards in slots 0-3 must be A,K,Q,J
                        result = 'Royal flush'
    return result
 
def test_flush(cards):
    result = 'n'
    suit_count = count_suits(cards)
    if any([suit_count[i] >= 5 for i in suit_count]):
            result = 'Flush'
    return result

def test_straight(cards):
    result = 'n'
    ranks = card_to_rank(cards)
    sranks = sorted(set(ranks), reverse = True)
    sranks.append(1) if card_rankings.index('A') + 2 in sranks else None #account for A being both high and low
    if any(sranks[i] - sranks[i+4] == 4 for i in range(len(sranks) - 4)):
        result = 'Straight'
    return result

def test_repeatrankhands(cards):
    result = 'n'
    sranks = set(card_to_rank(cards))
    rank_count = card_to_rankcount(cards)
    #counting the number of pairs, three of a kind, and four of a kind
    rcc = {j + 1 : 0 for j in range(4)}
    for i in sranks:
        rcc[rank_count[i]] += 1
    if rcc[4] >= 1:
        result = 'Four of a kind'
        return result
    elif rcc[3] >= 2 or (rcc[3] == 1 and rcc[2] >= 1):
        result = 'Full house'
        return result
    elif rcc[3] == 1:
        result = 'Three of a kind'
        return result
    elif rcc[2] >= 2:
        result = 'Two pairs'
        return result
    elif rcc[2] == 1:
        result = 'Pair'
        return result
    else:
        result = 'Highcard'
    return result


def card_to_rankcount(cards):
    ranks = card_to_rank(cards)
    rank_count = {i : ranks.count(i) for i in ranks}
    return rank_count

def card_to_rank(cards):
    unsorted_ranks = []
    for i in cards:
        unsorted_ranks.append(card_rankings.index(i[0]) + 2)
    ranks = sorted(unsorted_ranks, reverse = True)
    return ranks

def count_suits(cards):
    suit_count = {j : 0 for j in card_suits}
    for i in cards:
        suit_count[i[1]] += 1
    return suit_count