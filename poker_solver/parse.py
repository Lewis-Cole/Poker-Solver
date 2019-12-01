"""Parses text inputs into the appropriate format."""


import itertools

from .rules import ranks, suits


def parse_board(board_text: str) -> list:
    """Returns list of cards from string of cards.
    
    >>> parse_board("9h6hQc")
    ["9h", "6h", "Qc"]
    """
    return [board_text[i : i + 2] for i in range(0, len(board_text), 2)]


def parse_range(range_text: str) -> list:
    """Returns list of holdings from equilab format string.
    
    >>> parse_range("JJ")
    ["JsJh", "JsJd", "JsJc", "JhJd", "JhJc", "JdJc"]
    """
    segment_list = range_text.split(",")

    # returns list of combos relating to given rank and pairs/suited/offsuit
    def get_pairs(rank: str) -> list:
        """Returns all pair combos of rank"""
        cards = [rank + suit for suit in suits]
        return [list(combo) for combo in itertools.combinations(cards, 2)]

    def get_suited(rank_1: str, rank_2: str) -> list:
        """Returns all suited combos of two ranks"""
        return [[rank_1 + suit, rank_2 + suit] for suit in suits]

    def get_offsuit(rank_1: str, rank_2: str) -> list:
        """Returns all offsuit combos of two ranks"""
        return [
            [rank_1 + suit_1, rank_2 + suit_2]
            for suit_1 in suits
            for suit_2 in suits
            if suit_1 != suit_2
        ]

    # returns list containing combos relating to segment
    def parse_segment(segment_text: str) -> list:
        """Returns all combos related to given segment"""
        # different types of segments:
        # "AhAs", "AA", "AKs", "AKo", "KK+", "AQs+",
        # "AQo+", "KK-QQ", "AQs-AJs", "AQo-AJo"

        # group by length:
        seg_length = len(segment_text)

        # len=2: "AA"
        if seg_length == 2:
            return get_pairs(segment_text[0])

        # len=3: "AKs", "AKo", "KK+"
        if seg_length == 3:
            if segment_text[2] == "s":
                return get_suited(segment_text[0], segment_text[1])
            if segment_text[2] == "o":
                return get_offsuit(segment_text[0], segment_text[1])
            # return pair combos for given pair and higher
            return list(
                itertools.chain.from_iterable(
                    get_pairs(rank)
                    for rank in ranks
                    if ranks.index(rank) >= ranks.index(segment_text[0])
                )
            )

        # len=4: "AhAs", "AQs+", "AQo+"
        if seg_length == 4:
            if segment_text[2] == "s":
                return list(
                    itertools.chain.from_iterable(
                        get_suited(segment_text[0], rank_2)
                        for rank_2 in ranks
                        if ranks.index(rank_2) >= ranks.index(segment_text[1])
                        and rank_2 != segment_text[0]
                    )
                )
            if segment_text[2] == "o":
                return list(
                    itertools.chain.from_iterable(
                        get_offsuit(segment_text[0], rank_2)
                        for rank_2 in ranks
                        if ranks.index(rank_2) >= ranks.index(segment_text[1])
                        and rank_2 != segment_text[0]
                    )
                )
            # if given as hand format just return as list
            return [segment_text]

        # len=5: "KK-QQ"
        if seg_length == 5:
            return list(
                itertools.chain.from_iterable(
                    get_pairs(rank)
                    for rank in ranks
                    if ranks.index(segment_text[0])
                    >= ranks.index(rank)
                    >= ranks.index(segment_text[3])
                )
            )

        # len=7: "AQs-AJs", "AQo-AJo"
        if seg_length == 7:
            if segment_text[2] == "s":
                return list(
                    itertools.chain.from_iterable(
                        get_suited(segment_text[0], rank_2)
                        for rank_2 in ranks
                        if ranks.index(segment_text[1])
                        >= ranks.index(rank_2)
                        >= ranks.index(segment_text[5])
                    )
                )
            return list(
                itertools.chain.from_iterable(
                    get_offsuit(segment_text[0], rank_2)
                    for rank_2 in ranks
                    if ranks.index(segment_text[1])
                    >= ranks.index(rank_2)
                    >= ranks.index(segment_text[5])
                )
            )

    return list(
        itertools.chain.from_iterable(
            parse_segment(segment) for segment in segment_list
        )
    )
