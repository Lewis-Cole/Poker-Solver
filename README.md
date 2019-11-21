# --------------------
#   Poker-Solver
# --------------------

------
TODO:

https://realpython.com/documenting-python-code/
------

# Order of files

# 1. rules.py
# 2. rank.py
# 3. suit.py
# 4. card.py
# 5. deck.py
# 6. hand.py
# 7. holding.py
# 8. calculate_equity.py
# 9. holding_range.py
# 10. compare_range.py
# 11. read_range.py
# 12. equity_distribution.py
# 13. graph_data.py



#   Current usage instructions:
#   - run python on cmd
#   - from card import createcard
#   - from read_range import read_range
#   - from equity_distribution import equity_data
#   - Use equilab to create range text e.g. "JJ-99,JTs,T9s,98s,AQo"
#   - Create range1 and range2 via: read_range("range_text")
#   - e.g. r1 = read_range("JJ-99,JTs,T9s,98s,AQo")
#   - Create board: [createcard(''), createcard(''), createcard('')]
#   - e.g. board = [createcard("Qd"), createcard("9d"), createcard("2s")]
#   - equity_data(range1, range2, board)
#   - This will produce a spreadsheet with the equity of each hand in range 1
#   - Use plot_graph from graph_data.py to create the equity distribution graph from this data