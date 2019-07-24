from hand import Hand
from card import card_ranks, card_suits

hand_values = ('Highcard', 'Pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 
                'Full house', 'Four of a kind', 'Straight flush', 'Royal flush')

def compare_hands(IP_hand, OOP_hand):
    Hand.determine_value(IP_hand)
    Hand.determine_value(OOP_hand)
    IP_rank = hand_values.index(IP_hand.value)
    OOP_rank = hand_values.index(OOP_hand.value)
    if IP_rank > OOP_rank:
        return 'IP wins'
    elif OOP_rank > IP_rank:
        return 'OOP wins'
    elif IP_rank == OOP_rank:
        return compare_same_value(IP_hand, OOP_hand, IP_hand.value)


def compare_same_value(IP_hand, OOP_hand, hand_value):
    IP_highcards = sorted([rank for rank, count in enumerate(IP_hand.rank_counts) if count == 1], reverse = True)
    OOP_highcards = sorted([rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 1], reverse = True)

    if hand_value == 'Highcard':
        for i in range(5):
            if IP_highcards[i] > OOP_highcards[i]:
                return 'IP wins'
            elif IP_highcards[i] < OOP_highcards[i]:
                return 'OOP wins'
            else: None
        return 'Split pot'

    if hand_value == 'Pair':
        IP_pair = [rank for rank, count in enumerate(IP_hand.rank_counts) if count == 2][0]
        OOP_pair = [rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 2][0]
        if IP_pair > OOP_pair:
            return 'IP wins'
        elif IP_pair < OOP_pair:
            return 'OOP wins'
        else:
            for i in range(3):
                if IP_highcards[i] > OOP_highcards[i]:
                    return 'IP wins'
                elif IP_highcards[i] < OOP_highcards[i]:
                    return 'OOP wins'
                else: None
            return 'Split pot'

    if hand_value == 'Two pairs':
        IP_pairs = sorted([rank for rank, count in enumerate(IP_hand.rank_counts) if count == 2], reverse = True)
        OOP_pairs = sorted([rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 2], reverse = True)
        for i in range(2):
            if IP_pairs[i] > OOP_pairs[i]:
                return 'IP wins'
            elif IP_pairs[i] < OOP_pairs[i]:
                return 'OOP wins'
            else:
                if IP_highcards[0] > OOP_highcards[0]:
                    return 'IP wins'
                elif IP_highcards[0] < OOP_highcards[0]:
                    return 'OOP wins'
                else:
                    return 'Split pot'
    
    if hand_value == 'Three of a kind':
        IP_three = [rank for rank, count in enumerate(IP_hand.rank_counts) if count == 3][0]
        OOP_three = [rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 3][0]
        if IP_three > OOP_three:
            return 'IP wins'
        elif IP_three < OOP_three:
            return 'OOP wins'
        else:
            for i in range(2):
                if IP_highcards[i] > OOP_highcards[i]:
                    return 'IP wins'
                elif IP_highcards[i] < OOP_highcards[i]:
                    return 'OOP wins'
                else: None
            return 'Split pot'
    
    if hand_value == 'Straight':
        IP_lead = max([IP_hand.ranks_set[rank] for rank in range(len(IP_hand.ranks_set) - 4) if IP_hand.ranks_set[rank] - IP_hand.ranks_set[rank+4] == 4])
        OOP_lead = max([OOP_hand.ranks_set[rank] for rank in range(len(OOP_hand.ranks_set) - 4) if OOP_hand.ranks_set[rank] - OOP_hand.ranks_set[rank+4] == 4])
        if IP_lead > OOP_lead:
            return 'IP wins'
        elif IP_lead < OOP_lead:
            return 'OOP wins'
        else:
            return 'Split pot'
    
    if hand_value == 'Flush':
        for i in range(5):
            if IP_hand.flush_ranks[i] > OOP_hand.flush_ranks[i]:
                return 'IP wins'
            elif IP_hand.flush_ranks[i] < OOP_hand.flush_ranks[i]:
                return 'OOP wins'
            else: None
        return 'Split pot'

    if hand_value == 'Full house':
        IP_threes = sorted([rank for rank, count in enumerate(IP_hand.rank_counts) if count == 3], reverse = True)
        OOP_threes = sorted([rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 3], reverse = True)
        if IP_threes[0] > OOP_threes[0]:
            return 'IP wins'
        elif IP_threes[0] < OOP_threes[0]:
            return 'OOP wins'
        else:
            if len(IP_threes) >= 2:
                IP_fullof = IP_threes[1]
            else:
                IP_fullof = sorted([rank for rank, count in enumerate(IP_hand.rank_counts) if count == 2], reverse = True)[0]
            if len(OOP_threes) >= 2:
                OOP_fullof = OOP_threes[1]
            else:
                OOP_fullof = sorted([rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 2], reverse = True)[0]
            if IP_fullof > OOP_fullof:
                return 'IP wins'
            elif IP_fullof < OOP_fullof:
                return 'OOP wins'
            else:
                return 'Split pot'

    if hand_value == 'Four of a kind':
        IP_four = [rank for rank, count in enumerate(IP_hand.rank_counts) if count == 4][0]
        OOP_four = [rank for rank, count in enumerate(OOP_hand.rank_counts) if count == 4][0]
        if IP_four > OOP_four:
            return 'IP wins'
        elif IP_four < OOP_four:
            return 'OOP wins'
        elif IP_highcards[0] > OOP_highcards[0]:
            return 'IP wins'
        elif IP_highcards[0] < OOP_highcards[0]:
            return 'OOP wins'
        else:
            return 'Split pot'
    
    if hand_value == 'Straight flush':
        IP_sflead = max([IP_hand.flush_ranks[rank] for rank in range(len(IP_hand.flush_ranks) - 4) if IP_hand.flush_ranks[rank] - IP_hand.flush_ranks[rank+4] == 4])
        OOP_sflead = max([OOP_hand.flush_ranks[rank] for rank in range(len(OOP_hand.flush_ranks) - 4) if OOP_hand.flush_ranks[rank] - OOP_hand.flush_ranks[rank+4] == 4])
        if IP_sflead > OOP_sflead:
            return 'IP wins'
        elif IP_sflead < OOP_sflead:
            return 'OOP wins'
        else:
            return 'Split pot'
    
    if hand_value == 'Royal flush':
        return 'Split pot'
