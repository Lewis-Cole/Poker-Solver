'''Take a set of cards and determine the strongest hand value.
'''

from deck import card_rankings, card_suits, deck, get_card


hand_values = ('Highcard', 'Pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 
                'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')


def determine_hand_value(cards):
    #test if cards are valid hand and fit criteria
    #give best possible hand from cards
    print('')


def valid_hand(cards):
    if type(cards) != list:
        return('ERROR - Cards should be given as a list')
    elif any([type(i) != str or len(i) != 2 for i in cards]):
        return('ERROR - Cards should be strings of length 2')
    elif any([not(j in deck) for j in cards]):
        return('ERROR - Cards not from specified deck')
    elif len(cards) != len(set(cards)):
        return('ERROR - Duplicate cards')
    else:
        return('Valid hand')


def test_straight_flush(cards):
    result = 'n'
    if test_flush(cards) == 'y':
        suit_count = count_suits(cards)
        for i in suit_count:
            if suit_count[i] >= 5:
                flush_cards = []
                for j in cards:
                    flush_cards.append(j) if j[1] == i else None
                if test_straight(flush_cards) == 'y':
                    result = 'y'
                    flush_ranks = card_to_rank(flush_cards)
                    sflush_ranks = sorted(flush_ranks, reverse = True)
                    if sflush_ranks[4] == 10:   #if member 4 is 10 then only higher cards in slots 0-3 must be A,K,Q,J
                        result = 'ROYAL'
    return result
 

def test_flush(cards):
    result = 'n'
    suit_count = count_suits(cards)
    if any([suit_count[i] >= 5 for i in suit_count]):
            result = 'y'
    return result


def test_straight(cards):
    result = 'n'
    ranks = card_to_rank(cards)
    ssranks = sorted(set(ranks), reverse = True)
    ssranks.append(1) if 14 in ssranks else None #account for A being both high and low
    if any(ssranks[i] - ssranks[i+4] == 4 for i in range(len(ssranks) - 4)):
        result = 'y'
    return result



def card_to_rankcount(cards):
    ranks = card_to_rank(cards)
    sranks = sorted(ranks, reverse = True)
    srank_count = {i : sranks.count(i) for i in sranks}
    return srank_count


def card_to_rank(cards):
    ranks = []
    for i in cards:
        ranks.append(card_rankings.index(i[0]) + 2)
    return ranks


def count_suits(cards):
    suit_count = {j : 0 for j in card_suits}
    for i in cards:
        suit_count[i[1]] += 1
    return suit_count

testcards = ['Kh', 'Kd', 'Kc', 'Ks', '7d', '7s', '4s']
test_fourofakind(testcards)
