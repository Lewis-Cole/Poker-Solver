# --------------------------------------------------------
#   This file contains functions for comparing ranges
# --------------------------------------------------------

# import here
from holding_range import Holding_Range
from compare_range import range_comparison
import xlsxwriter as xlwt

# method of measuring the distribution of equity across a range
def equity_data(IP_range, OOP_range, board):

    def gen_hold_equities(IP_r, OOP_r, boa):
        for holding in IP_r.holdings:
            IP_sr = Holding_Range([holding])
            result = range_comparison(IP_sr, OOP_r, boa)

            yield holding, result[0]

    data_set = list(gen_hold_equities(IP_range, OOP_range, board))

    # creating excel file
    workbook = xlwt.Workbook('Equity_Distribution_Data.xlsx')
    worksheet = workbook.add_worksheet()

    # titling columns
    worksheet.write(0, 0, 'Holdings')
    worksheet.write(0, 1, 'Equity')

    row = 1
    
    for item in data_set:
        worksheet.write(row, 0, item[0].__repr__())
        worksheet.write(row, 1, item[1])

        row += 1
    
    workbook.close()