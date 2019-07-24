from card import Card, card_ranks, card_suits
from hand import Hand
from deck import Deck
from comparehands import compare_hands

def calculate_equity(IP_holding, OOP_holding, board):
    deck = Deck(card_ranks, card_suits)
    dead_cards = IP_holding + OOP_holding + board
    deck.remove_dead_cards(dead_cards)
    cards_to_deal = 5 - len(board)

    IP_wins = 0.0
    OOP_wins = 0.0

    while True:
        for _ in range(10000):
            onto_board = list(deck.get_cards(cards_to_deal))
            IP_hand = Hand(IP_holding + board + onto_board)
            OOP_hand = Hand(OOP_holding + board + onto_board)
            result = compare_hands(IP_hand, OOP_hand)
            if result == 'IP wins':
                IP_wins += 1
            elif result == 'OOP wins':
                OOP_wins += 1
            else:
                IP_wins += 0.5
                OOP_wins += 0.5
            IP_EQ = 100 * IP_wins / (IP_wins + OOP_wins)
            OOP_EQ = 100 * OOP_wins / (IP_wins + OOP_wins)
        print('IP equity = ' + str(IP_EQ) + '%')
        print('OOP equity = ' + str(OOP_EQ) + '%')
    return (IP_EQ, OOP_EQ)