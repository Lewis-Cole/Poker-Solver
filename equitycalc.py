''' Calculate equity of two hands in given scenario.
'''

from deck import full_deck, get_card
from hand_values import compare_hands


def calculate_equity(IP_holding, OOP_holding, board):
    dead_cards = IP_holding + OOP_holding + board
    deck = []
    for i in full_deck:
        deck.append(i)
    for i in dead_cards:
        deck.remove(i)
    cards_to_deal = 5 - len(board)
    
    IP_wins = 0.0
    OOP_wins = 0.0

    while True:
        for i in range (100000):
            onto_board = list(get_card(deck, cards_to_deal))
            total_board = board + onto_board
            IP_cards = IP_holding + total_board
            OOP_cards = OOP_holding + total_board
            x = compare_hands(IP_cards, OOP_cards)
            if x == 'IP wins':
                IP_wins += 1
            elif x == 'OOP wins':
                OOP_wins += 1
            elif x == 'Split pot':
                IP_wins += 0.5
                OOP_wins += 0.5
        IP_EQ = 100 * IP_wins / (IP_wins + OOP_wins)
        OOP_EQ = 100 * OOP_wins / (IP_wins + OOP_wins)
        print('IP equity = ' + str(IP_EQ) + '%')
        print('OOP equity = ' + str(OOP_EQ) + '%')
    return (IP_EQ, OOP_EQ)

