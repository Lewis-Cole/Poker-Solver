'''Take a set of cards and determine the strongest hand value.
'''

from deck import card_rankings, card_suits, deck


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
    elif any([not(i in deck) for i in cards]):
        return('ERROR - Cards not from specified deck')
    elif len(cards) != len(set(cards)):
        return('ERROR - Duplicate cards')
    else:
        return('Valid hand')


def test_flush(cards):
    result = 'n'
    suit_count = count_suits(cards)
    if any([suit_count[i] >= 5 for i in cards]):
            result = 'y'
    return result


def count_suits(cards):
    suit_count = {i : 0 for i in card_suits}
    for i in cards:
        suit_count[i[1]] += 1
    return suit_count


def test_straight(cards):
    result = 'n'
    print([(i[0] + 2, i[1]) for i in list(enumerate(card_rankings))])
    return result

print(test_straight(['Ah', 'Kh', 'Qh', 'Jh', 'Th']))