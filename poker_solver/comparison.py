"""Contains comparison functions."""


import itertools

from .rules import ranks, suits
from .hand import Hand


def compare_ranges(IP_range: list, OOP_range: list, board: list) -> dict:
    """Returns equities of each holding in IP_range vs OOP_range on board"""
    # accounting for range blocked by board
    IP_range = [
        hand for hand in IP_range if (hand[0] not in board) and (hand[1] not in board)
    ]
    OOP_range = [
        hand for hand in OOP_range if (hand[0] not in board) and (hand[1] not in board)
    ]

    IP_equity_dict = {"".join(IP_holding): 0 for IP_holding in IP_range}
    for IP_holding in IP_range:
        OOP_range_part = [
            hand
            for hand in OOP_range
            if (hand[0] not in IP_holding) and (hand[1] not in IP_holding)
        ]
        equity_list = [
            IP_equity
            for (IP_equity, _) in [
                compare_holdings(IP_holding, OOP_holding, board)
                for OOP_holding in OOP_range_part
            ]
        ]
        avg_equity = round(sum(equity_list) / len(equity_list), 2)
        IP_equity_dict["".join(IP_holding)] = avg_equity

    return IP_equity_dict


def compare_holdings(
    IP_holding: list, OOP_holding: list, board: list
) -> (float, float):
    """Returns equity of each holding on given board."""
    # preparing deck of remaining cards
    deck = ["".join(element) for element in itertools.product(ranks, suits)]
    dead_cards = list(itertools.chain(IP_holding, OOP_holding, board))
    for card in dead_cards:
        if card in deck:
            deck.remove(card)

    cards_to_deal = 5 - len(board)

    IP_wins = 0.0
    OOP_wins = 0.0

    # On the river - whole board dealt
    if cards_to_deal == 0:
        IP_hand = Hand(IP_holding + board)
        OOP_hand = Hand(OOP_holding + board)

        if IP_hand > OOP_hand:
            IP_wins += 1
        elif IP_hand < OOP_hand:
            OOP_wins += 1
        else:
            IP_wins += 0.5
            OOP_wins += 0.5

        total_runouts = IP_wins + OOP_wins

        IP_equity = round(100 * IP_wins / total_runouts, 2)
        OOP_equity = round(100 * OOP_wins / total_runouts, 2)

        return (IP_equity, OOP_equity)

    # On the turn
    if cards_to_deal == 1:
        for card in deck:
            final_board = board + [card]
            IP_hand = Hand(IP_holding + final_board)
            OOP_hand = Hand(OOP_holding + final_board)

            if IP_hand > OOP_hand:
                IP_wins += 1
            elif IP_hand < OOP_hand:
                OOP_wins += 1
            else:
                IP_wins += 0.5
                OOP_wins += 0.5

        total_runouts = IP_wins + OOP_wins

        IP_equity = round(100 * IP_wins / total_runouts, 2)
        OOP_equity = round(100 * OOP_wins / total_runouts, 2)

        return (IP_equity, OOP_equity)

    # On the flop
    if cards_to_deal == 2:
        for combo in itertools.combinations(deck, 2):
            final_board = board + list(combo)
            IP_hand = Hand(IP_holding + final_board)
            OOP_hand = Hand(OOP_holding + final_board)

            if IP_hand > OOP_hand:
                IP_wins += 1
            elif IP_hand < OOP_hand:
                OOP_wins += 1
            else:
                IP_wins += 0.5
                OOP_wins += 0.5

        total_runouts = IP_wins + OOP_wins

        IP_equity = round(100 * IP_wins / total_runouts, 2)
        OOP_equity = round(100 * OOP_wins / total_runouts, 2)

        return (IP_equity, OOP_equity)

    # Preflop
    if cards_to_deal == 5:
        for combo in itertools.combinations(deck, 5):
            final_board = board + list(combo)
            IP_hand = Hand(IP_holding + final_board)
            OOP_hand = Hand(OOP_holding + final_board)

            if IP_hand > OOP_hand:
                IP_wins += 1
            elif IP_hand < OOP_hand:
                OOP_wins += 1
            else:
                IP_wins += 0.5
                OOP_wins += 0.5

        total_runouts = IP_wins + OOP_wins

        IP_equity = round(100 * IP_wins / total_runouts, 2)
        OOP_equity = round(100 * OOP_wins / total_runouts, 2)

        return (IP_equity, OOP_equity)
