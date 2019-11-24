"""Tests other modules."""


# from .parse import parse_board, parse_range
# from .hand import Hand
# from .comparison import compare_holdings, compare_ranges
from .graph import plot_graph


# print("---")

# # testing parse.py
# print(parse_board("9h6hQc") == ["9h", "6h", "Qc"])

# print(
#     parse_range("JJ-99,98s,AKo")
#     == [
#         ["9c", "9d"],
#         ["9c", "9h"],
#         ["9c", "9s"],
#         ["9d", "9h"],
#         ["9d", "9s"],
#         ["9h", "9s"],
#         ["Tc", "Td"],
#         ["Tc", "Th"],
#         ["Tc", "Ts"],
#         ["Td", "Th"],
#         ["Td", "Ts"],
#         ["Th", "Ts"],
#         ["Jc", "Jd"],
#         ["Jc", "Jh"],
#         ["Jc", "Js"],
#         ["Jd", "Jh"],
#         ["Jd", "Js"],
#         ["Jh", "Js"],
#         ["9c", "8c"],
#         ["9d", "8d"],
#         ["9h", "8h"],
#         ["9s", "8s"],
#         ["Ac", "Kd"],
#         ["Ac", "Kh"],
#         ["Ac", "Ks"],
#         ["Ad", "Kc"],
#         ["Ad", "Kh"],
#         ["Ad", "Ks"],
#         ["Ah", "Kc"],
#         ["Ah", "Kd"],
#         ["Ah", "Ks"],
#         ["As", "Kc"],
#         ["As", "Kd"],
#         ["As", "Kh"],
#     ]
# )

# print("---")

# # testing Hand.determine_value in hand.py
# hand1 = Hand(["As", "Kc", "5d", "Ac", "Kd", "Ah", "5s"])
# print(hand1.value == "Full house")

# hand2 = Hand(["As", "2c", "3d", "5c", "Td", "9h", "4s"])
# print(hand2.value == "Straight")

# hand3 = Hand(["8s", "9s", "Ad", "5c", "Qs", "Ts", "Js"])
# print(hand3.value == "Straight flush")

# print("---")

# # testing comparison methods of Hand in hand.py
# hand4 = Hand(["As", "2c", "6d", "Ac", "3d", "7h", "5s"])
# hand5 = Hand(["7s", "2c", "3d", "Ac", "Td", "9h", "As"])
# hand6 = Hand(["8s", "9s", "9d", "5c", "8s", "Ts", "8s"])
# hand7 = Hand(["8s", "9s", "Ad", "8c", "9s", "Ts", "9s"])

# print((hand4 > hand5) == False)
# print((hand5 > hand6) == False)
# print((hand6 > hand7) == False)

# print("---")

# # testing comparison.py
# print(
#     compare_holdings(["Ac", "Kc"], ["Jd", "Jh"], parse_board("9h6hQc"))
#     == (26.16, 73.84)
# )

# range1 = parse_range("JJ-99,98s")
# range2 = parse_range("AA,AKs")
# board = parse_board("9h6hQc")
# print(
#     compare_ranges(range1, range2, board)
#     == {
#         "9c9d": 90.26,
#         "9c9s": 90.26,
#         "9d9s": 90.26,
#         "TcTd": 34.83,
#         "TcTh": 37.08,
#         "TcTs": 34.83,
#         "TdTh": 37.02,
#         "TdTs": 34.76,
#         "ThTs": 37.02,
#         "JcJd": 33.89,
#         "JcJh": 36.13,
#         "JcJs": 33.89,
#         "JdJh": 36.07,
#         "JdJs": 33.83,
#         "JhJs": 36.07,
#         "9c8c": 43.63,
#         "9d8d": 40.68,
#         "9s8s": 40.68,
#     }
# )

# print("---")

# plot_graph(
#     "22+,A2s+,K9s+,Q9s+,J9s+,T9s,98s,87s,ATo+,KJo+",
#     "TT-22,ATs-A2s,KJs-K6s,Q8s+,J8s+,T8s+,97s+,86s+,75s+,65s,54s,AQo-AJo,KQo",
#     "9h6hQc",
# )

print("---")

plot_graph(
    "22+,A2s+,K9s+,QTs+,J9s+,T9s,98s,87s,76s,ATo+,KJo+",
    "TT-22,ATs-A2s,KJs-K5s,QTs-Q8s,J8s+,T8s+,97s+,86s+,75s+,64s+,54s,AQo-ATo,KJo+",
    "Kh8s4c",
    "test_graph",
)
