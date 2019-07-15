'''Take two sets of cards and determine which wins or split pot.
'''

from deck import card_rankings, card_suits, full_deck


hand_values = ('Highcard', 'Pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 
                'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')


def compare_hands(IP_cards, OOP_cards):
    IP_value = determine_hand_value(IP_cards)
    OOP_value = determine_hand_value(OOP_cards)
    IP_rank = hand_values.index(IP_value)
    OOP_rank = hand_values.index(OOP_value)
    if IP_rank > OOP_rank:
        return 'IP wins'
    elif OOP_rank > IP_rank:
        return 'OOP wins'
    elif IP_rank == OOP_rank:
        return compare_same_value(IP_cards, OOP_cards, IP_value)


def compare_same_value(IP_cards, OOP_cards, hand_value):
    IP_ranks = card_to_rank(IP_cards)
    OOP_ranks = card_to_rank(OOP_cards)
    IP_rankcount = card_to_rankcount(IP_cards)
    OOP_rankcount = card_to_rankcount(OOP_cards)
    
    if hand_value == 'Highcard':
        for i in range(5):
            if IP_ranks[i] > OOP_ranks[i]:
                return 'IP wins'
            elif IP_ranks[i] < OOP_ranks[i]:
                return 'OOP wins'
            else: None
        return 'Split pot'

    if hand_value == 'Pair':
        IP_pair = [i for (i, j) in IP_rankcount.items() if j == 2][0]
        OOP_pair = [i for (i, j) in OOP_rankcount.items() if j == 2][0]
        if IP_pair > OOP_pair:
            return 'IP wins'
        elif IP_pair < OOP_pair:
            return 'OOP wins'
        else:
            IP_ranks.remove(IP_pair)
            IP_ranks.remove(IP_pair)
            OOP_ranks.remove(OOP_pair)
            OOP_ranks.remove(OOP_pair)
            for i in range(3):
                if IP_ranks[i] > OOP_ranks[i]:
                    return 'IP wins'
                elif IP_ranks[i] < OOP_ranks[i]:
                    return 'OOP wins'
                else: None
            return 'Split pot'

    if hand_value == 'Two pairs':
        IP_pairs = sorted([i for (i, j) in IP_rankcount.items() if j == 2], reverse = True)
        OOP_pairs = sorted([i for (i, j) in OOP_rankcount.items() if j == 2], reverse = True)
        for i in range(2):
            if IP_pairs[i] > OOP_pairs[i]:
                return 'IP wins'
            elif IP_pairs[i] < OOP_pairs[i]:
                return 'OOP wins'
            else:
                IP_ranks.remove(IP_pairs[0])
                IP_ranks.remove(IP_pairs[0])
                IP_ranks.remove(IP_pairs[1])
                IP_ranks.remove(IP_pairs[1])
                OOP_ranks.remove(OOP_pairs[0])
                OOP_ranks.remove(OOP_pairs[0])
                OOP_ranks.remove(OOP_pairs[1])
                OOP_ranks.remove(OOP_pairs[1])
                if IP_ranks[0] > OOP_ranks[0]:
                    return 'IP wins'
                elif IP_ranks[0] < OOP_ranks[0]:
                    return 'OOP wins'
                else:
                    return 'Split pot'
    
    if hand_value == 'Three of a kind':
        IP_three = [i for (i, j) in IP_rankcount.items() if j == 3][0]
        OOP_three = [i for (i, j) in OOP_rankcount.items() if j == 3][0]
        if IP_three > OOP_three:
            return 'IP wins'
        elif IP_three < OOP_three:
            return 'OOP wins'
        else:
            for i in range(3):
                IP_ranks.remove(IP_three)
                OOP_ranks.remove(OOP_three)
            for i in range(2):
                if IP_ranks[i] > OOP_ranks[i]:
                    return 'IP wins'
                elif IP_ranks[i] < OOP_ranks[i]:
                    return 'OOP wins'
                else: None
            return 'Split pot'
    
    if hand_value == 'Straight':
        IP_sranks = sorted(set(IP_ranks), reverse = True)
        IP_sranks.append(1) if card_rankings.index('A') + 2 in IP_sranks else None
        OOP_sranks = sorted(set(OOP_ranks), reverse = True)
        OOP_sranks.append(1) if card_rankings.index('A') + 2 in OOP_sranks else None
        IP_lead = max([IP_sranks[i] for i in range(len(IP_sranks) - 4) if IP_sranks[i] - IP_sranks[i+4] == 4])
        OOP_lead = max([OOP_sranks[i] for i in range(len(OOP_sranks) - 4) if OOP_sranks[i] - OOP_sranks[i+4] == 4])
        if IP_lead > OOP_lead:
            return 'IP wins'
        elif IP_lead < OOP_lead:
            return 'OOP wins'
        else:
            return 'Split pot'
    
    if hand_value == 'Flush':
        IP_suit_count = count_suits(IP_cards)
        for i in IP_suit_count:
            if IP_suit_count[i] >= 5:
                IP_flush_cards = []
                for j in IP_cards:
                    IP_flush_cards.append(j) if j[1] == i else None
                IP_flush_ranks = card_to_rank(IP_flush_cards)
        OOP_suit_count = count_suits(OOP_cards)
        for i in OOP_suit_count:
            if OOP_suit_count[i] >= 5:
                OOP_flush_cards = []
                for j in OOP_cards:
                    OOP_flush_cards.append(j) if j[1] == i else None
                OOP_flush_ranks = card_to_rank(OOP_flush_cards)
        for i in range(5):
            if IP_flush_ranks[i] > OOP_flush_ranks[i]:
                return 'IP wins'
            elif IP_flush_ranks[i] < OOP_flush_ranks[i]:
                return 'OOP wins'
            else: None
        return 'Split pot'

    if hand_value == 'Full house':
        IP_house = [i for (i, j) in IP_rankcount.items() if j == 3][0]
        OOP_house = [i for (i, j) in OOP_rankcount.items() if j == 3][0]
        if IP_house > OOP_house:
            return 'IP wins'
        elif IP_house < OOP_house:
            return 'OOP wins'
        else:
            for i in range(3):
                IP_ranks.remove(IP_house)
                OOP_ranks.remove(OOP_house)
                IP_rankcountnew = card_to_rankcount(IP_cards)
                OOP_rankcountnew = card_to_rankcount(OOP_cards)
            IP_fullof = [i for (i, j) in IP_rankcountnew.items() if j >= 2][0]
            OOP_fullof = [i for (i, j) in OOP_rankcountnew.items() if j >= 2][0]
            if IP_fullof > OOP_fullof:
                return 'IP wins'
            elif IP_fullof < OOP_fullof:
                return 'OOP wins'
            else:
                return 'Split pot'

    if hand_value == 'Four of a kind':
        IP_four = [i for (i, j) in IP_rankcount.items() if j == 4][0]
        OOP_four = [i for (i, j) in OOP_rankcount.items() if j == 4][0]
        if IP_four > OOP_four:
            return 'IP wins'
        elif IP_four < OOP_four:
            return 'OOP wins'
        else:
            for i in range (4):
                IP_ranks.remove(IP_four)
                OOP_ranks.remove(OOP_four)
            if IP_ranks[0] > OOP_ranks[0]:
                return 'IP wins'
            elif IP_ranks[0] < OOP_ranks[0]:
                return 'OOP wins'
            else: None
        return 'Split pot'
    
    if hand_value == 'Straight flush':
        IP_suit_count = count_suits(IP_cards)
        for i in IP_suit_count:
            if IP_suit_count[i] >= 5:
                IP_flush_cards = []
                for j in IP_cards:
                    IP_flush_cards.append(j) if j[1] == i else None
                if test_straight(IP_flush_cards) == 'Straight':
                    IP_flush_ranks = card_to_rank(IP_flush_cards)
                    IP_flush_sranks = sorted(set(IP_flush_ranks), reverse = True)
                    IP_flush_sranks.append(1) if card_rankings.index('A') + 2 in IP_flush_sranks else None
                    IP_sflead = max([IP_flush_sranks[i] for i in range(len(IP_flush_sranks) - 4) if IP_flush_sranks[i] - IP_flush_sranks[i+4] == 4])
        
        OOP_suit_count = count_suits(OOP_cards)
        for i in OOP_suit_count:
            if OOP_suit_count[i] >= 5:
                OOP_flush_cards = []
                for j in OOP_cards:
                    OOP_flush_cards.append(j) if j[1] == i else None
                if test_straight(OOP_flush_cards) == 'Straight':
                    OOP_flush_ranks = card_to_rank(OOP_flush_cards)
                    OOP_flush_sranks = sorted(set(OOP_flush_ranks), reverse = True)
                    OOP_flush_sranks.append(1) if card_rankings.index('A') + 2 in OOP_flush_sranks else None
                    OOP_sflead = max([OOP_flush_sranks[i] for i in range(len(OOP_flush_sranks) - 4) if OOP_flush_sranks[i] - OOP_flush_sranks[i+4] == 4])
        
        if IP_sflead > OOP_sflead:
            return 'IP wins'
        elif IP_sflead < OOP_sflead:
            return 'OOP wins'
        else:
            return 'Split pot'

    if hand_value == 'Royal flush':
        return 'Split pot'


def determine_hand_value(cards):
    if valid_hand(cards) != 'Valid hand':
        print(valid_hand(cards))
        exit()

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
    elif any([not(j in full_deck) for j in cards]):
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
                    sflush_ranks.append(1) if card_rankings.index('A') + 2 in sflush_ranks else None
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

