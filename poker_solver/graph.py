"""Contains functions for graphing and plotting data."""


import matplotlib.pyplot
import xlsxwriter

from .parse import parse_board, parse_range
from .comparison import compare_ranges


def plot_graph(
    IP_range_text: str,
    OOP_range_text: str,
    board_text: str,
    filename: str = "default_name",
):
    """Plot equity graph for IP range"""
    # parsing text
    IP_range = parse_range(IP_range_text)
    OOP_range = parse_range(OOP_range_text)
    board = parse_board(board_text)

    # compute equities
    IP_equity_dict = compare_ranges(IP_range, OOP_range, board)

    # make and save spreadsheet
    workbook_filepath = "".join(["spreadsheets/", filename, ".xlsx"])
    workbook = xlsxwriter.Workbook(workbook_filepath)
    worksheet = workbook.add_worksheet()

    row = 0
    column = 0

    for holding, equity in IP_equity_dict.items():
        worksheet.write(row, column, holding)
        worksheet.write(row, column + 1, equity)
        row += 1

    workbook.close()

    # make and save graph
    equity_data = [IP_equity_dict[key] for key in IP_equity_dict]

    matplotlib.pyplot.hist(
        equity_data, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,],
    )
    matplotlib.pyplot.axis([0, 100, 0, 150])

    graph_filepath = "".join(["graphs/", filename, ".png"])
    matplotlib.pyplot.savefig(graph_filepath)
    matplotlib.pyplot.close()
