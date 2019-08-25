from rank import Rank, ranks
from suit import Suit, suits
from card import Card
from hand import Hand
from deck import Deck

def monte_carlo(IP_holding, OOP_holding, board, iterations):
    deck = Deck(ranks, suits)
    dead_cards = IP_holding + OOP_holding + board
    deck.remove(dead_cards)
    cards_to_deal = 5 - len(board)
    
    IP_wins = 0.0
    OOP_wins = 0.0

    print('0 of ' + str(iterations) + ' complete')

    for index in range(iterations):
        deck.shuffle()
        dealt_cards = deck.get(cards_to_deal)
        IP_hand = Hand(IP_holding + board + dealt_cards)
        OOP_hand = Hand(OOP_holding + board + dealt_cards)
        
        if IP_hand > OOP_hand:
            IP_wins += 1
        elif IP_hand < OOP_hand:
            OOP_wins += 1
        elif IP_hand == OOP_hand:
            IP_wins += 0.5
            OOP_wins += 0.5
        
        if (index + 1) % 10000 == 0:
            print(str(index + 1) + ' of ' + str(iterations) + ' complete')
            print(round(100 * IP_wins / (IP_wins + OOP_wins), 2), round(100 * OOP_wins / (IP_wins + OOP_wins), 2))

    IP_EQ = round(100 * IP_wins / (IP_wins + OOP_wins), 2)
    OOP_EQ = round(100 * OOP_wins / (IP_wins + OOP_wins), 2)
    return (IP_EQ, OOP_EQ)

def enumerate_all(IP_holding, OOP_holding, board):
    deck = Deck(ranks, suits)
    dead_cards = IP_holding + OOP_holding + board
    deck.remove(dead_cards)
    cards_to_deal = 5 - len(board)
    
    IP_wins = 0.0
    OOP_wins = 0.0

    if cards_to_deal == 1:
        for card in deck.cards:
            IP_hand = Hand(IP_holding + board + [card])
            OOP_hand = Hand(OOP_holding + board + [card])
            
            if IP_hand > OOP_hand:
                IP_wins += 1
            elif IP_hand < OOP_hand:
                OOP_wins += 1
            elif IP_hand == OOP_hand:
                IP_wins += 0.5
                OOP_wins += 0.5
        IP_EQ = round(100 * IP_wins / (IP_wins + OOP_wins), 2)
        OOP_EQ = round(100 * OOP_wins / (IP_wins + OOP_wins), 2)
        return (IP_EQ, OOP_EQ)
    
    if cards_to_deal == 2:
        for card1 in deck.cards:
            for card2 in deck.cards:
                if card1 != card2:
                    IP_hand = Hand(IP_holding + board + [card1, card2])
                    OOP_hand = Hand(OOP_holding + board + [card1, card2])
                    
                    if IP_hand > OOP_hand:
                        IP_wins += 1
                    elif IP_hand < OOP_hand:
                        OOP_wins += 1
                    elif IP_hand == OOP_hand:
                        IP_wins += 0.5
                        OOP_wins += 0.5
        IP_EQ = round(100 * IP_wins / (IP_wins + OOP_wins), 2)
        OOP_EQ = round(100 * OOP_wins / (IP_wins + OOP_wins), 2)
        return (IP_EQ, OOP_EQ)
    
    if cards_to_deal == 5:
        #note this takes too long to use rn
        for card1 in deck.cards:
            for card2 in deck.cards:
                if card1 != card2:
                    for card3 in deck.cards:
                        if card1 != card3 and card2 != card3:
                            for card4 in deck.cards:
                                if card1 != card4 and card2 != card4 and card3 != card4:
                                    for card5 in deck.cards:
                                        if card1 != card5 and card2 != card5 and card3 != card5 and card4 != card5:
                                            IP_hand = Hand(IP_holding + board + [card1, card2, card3, card4, card5])
                                            OOP_hand = Hand(OOP_holding + board + [card1, card2, card3, card4, card5])
                                            
                                            if IP_hand > OOP_hand:
                                                IP_wins += 1
                                            elif IP_hand < OOP_hand:
                                                OOP_wins += 1
                                            elif IP_hand == OOP_hand:
                                                IP_wins += 0.5
                                                OOP_wins += 0.5
        IP_EQ = round(100 * IP_wins / (IP_wins + OOP_wins), 2)
        OOP_EQ = round(100 * OOP_wins / (IP_wins + OOP_wins), 2)
        return (IP_EQ, OOP_EQ)