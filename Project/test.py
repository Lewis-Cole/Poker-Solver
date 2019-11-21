from card import createcard
from read_range import read_range
from equity_distribution import equity_data

r1 = read_range("QQ+,AKs")
r2 = read_range("JJ-99,98s")

board = [createcard("Qd"), createcard("9d"), createcard("2s")]

equity_data(r1, r2, board)
