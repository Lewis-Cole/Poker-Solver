"""Make the database for hand categorisation."""


import json
import itertools

from .rules import ranks


straight_ranks = ["A"] + list(ranks)


def test_straight(ranks_in_hand) -> (bool, str):
    """Return bool of if straight and lead card"""
    count = 0
    made_straight = False
    for rank in straight_ranks:
        if rank in ranks_in_hand:
            last_rank = rank
            count += 1
        else:
            if made_straight == True:
                return (True, last_rank)
            count = 0
        if count == 5:
            made_straight = True
    if made_straight == True:
        return (True, last_rank)

    return (False, None)


data = {}

for n in range(2, 8):
    for combo in itertools.combinations(ranks, n):
        ranks_in_hand = sorted(set(combo))
        result = test_straight(ranks_in_hand)
        data[str(ranks_in_hand)] = result


with open("poker_solver/data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
