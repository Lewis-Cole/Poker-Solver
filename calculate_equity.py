# --------------------------------------------------------
#   This file contains functions for calculating equity
# --------------------------------------------------------

# import here
from hand import Hand
from deck import deck


# method of enumerating every possible branch
def eq_enumeration(IP_holding, OOP_holding, board):
    deck.replenish()    
    dead_cards = IP_holding.cards + OOP_holding.cards + board
    deck.remove(dead_cards)
    cards_to_deal = 5 - len(board)

    IP_wins = 0.0
    OOP_wins = 0.0

    if cards_to_deal == 0:
        IP_hand = Hand(IP_holding.cards + board)
        OOP_hand = Hand(OOP_holding.cards + board)

        if IP_hand > OOP_hand:
            IP_wins += 1
        elif OOP_hand > IP_hand:
            OOP_wins += 1
        elif IP_hand == OOP_hand:
            IP_wins += 0.5
            OOP_wins += 0.5
        
        total_runs = IP_wins + OOP_wins
            
        IP_EQ = round(100 * IP_wins / total_runs, 2)
        OOP_EQ = round(100 * OOP_wins / total_runs, 2)

        return IP_EQ, OOP_EQ

    if cards_to_deal == 1:
        for card in deck.cards:
            final_board = board + [card]
            IP_hand = Hand(IP_holding.cards + final_board)
            OOP_hand = Hand(OOP_holding.cards + final_board)

            if IP_hand > OOP_hand:
                IP_wins += 1
            elif OOP_hand > IP_hand:
                OOP_wins += 1
            elif IP_hand == OOP_hand:
                IP_wins += 0.5
                OOP_wins += 0.5

        total_runs = IP_wins + OOP_wins

        IP_EQ = round(100 * IP_wins / total_runs, 2)
        OOP_EQ = round(100 * OOP_wins / total_runs, 2)
        
        return IP_EQ, OOP_EQ
    
    if cards_to_deal == 2:
        num_deck = len(deck.cards)
        for index1 in range(num_deck - 1):
            for index2 in range(index1 + 1, num_deck):
                final_board = board + [deck.cards[index1], deck.cards[index2]]
                IP_hand = Hand(IP_holding.cards + final_board)
                OOP_hand = Hand(OOP_holding.cards + final_board)

                if IP_hand > OOP_hand:
                    IP_wins += 1
                elif OOP_hand > IP_hand:
                    OOP_wins += 1
                elif IP_hand == OOP_hand:
                    IP_wins += 0.5
                    OOP_wins += 0.5

        total_runs = IP_wins + OOP_wins

        IP_EQ = round(100 * IP_wins / total_runs, 2)
        OOP_EQ = round(100 * OOP_wins / total_runs, 2)
        
        return IP_EQ, OOP_EQ
    
    if cards_to_deal == 5:
        num_deck = len(deck.cards)
        for index1 in range(num_deck - 4):
            for index2 in range(index1 + 1, num_deck - 3):
                for index3 in range(index2 + 1, num_deck - 2):
                    for index4 in range(index3 + 1, num_deck - 1):
                        for index5 in range(index4 + 1, num_deck):
                            final_board = [deck.cards[index1], deck.cards[index2], deck.cards[index3], deck.cards[index4], deck.cards[index5]]
                            IP_hand = Hand(IP_holding.cards + final_board)
                            OOP_hand = Hand(OOP_holding.cards + final_board)

                            if IP_hand > OOP_hand:
                                IP_wins += 1
                            elif OOP_hand > IP_hand:
                                OOP_wins += 1
                            elif IP_hand == OOP_hand:
                                IP_wins += 0.5
                                OOP_wins += 0.5

        total_runs = IP_wins + OOP_wins
        
        IP_EQ = round(100 * IP_wins / total_runs, 2)
        OOP_EQ = round(100 * OOP_wins / total_runs, 2)
        
        return IP_EQ, OOP_EQ