# --------------------------------------------------------
#   This file contains functions for comparing ranges
# --------------------------------------------------------

# import here
from calculate_equity import eq_enumeration

# method of enumerating every possible branch
def range_comparison(IP_range, OOP_range, board):
    results = []

    for IP_holding in IP_range.holdings:
        for OOP_holding in OOP_range.holdings:
            # checking if the board blocks this holding
            if not(any(card in board for card in IP_holding.cards + OOP_holding.cards)):
                # checking if one holding blocks the other
                if not(any(card in IP_holding.cards for card in OOP_holding.cards)):
                    results.append(eq_enumeration(IP_holding, OOP_holding, board))
    
    num = len(results)
    cumulative_result = [0,0]
    for (eq1, eq2) in results:
        cumulative_result[0] += eq1
        cumulative_result[1] += eq2
    
    average_result = (round(cumulative_result[0]/num, 2), round(cumulative_result[1]/num, 2))

    return average_result