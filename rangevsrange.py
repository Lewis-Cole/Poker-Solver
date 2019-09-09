from hrange import HRange
from equitycalc import enumerate_all as enum

def rangevsrange_calc(hrange1, hrange2, board):
    results = []
    for holding1 in hrange1.holdings:
        for holding2 in hrange2.holdings:
            result = enum(holding1, holding2, board)
            results.append(result)
    
    num = len(results)
    cumulative_res = [0,0]
    for (eq1, eq2) in results:
        cumulative_res[0] += eq1
        cumulative_res[1] += eq2
    
    adjusted_res = (round(cumulative_res[0]/num, 2), round(cumulative_res[1]/num, 2))

    return adjusted_res