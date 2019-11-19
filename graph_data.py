# ----------------------------------------------------------------------
#   This file contains a function for graphinh the equity distribution
# ----------------------------------------------------------------------

# import here
import xlrd
import xlsxwriter as xlwt

# method of preparing data for distribution plot
def plot_graph(distinct_sets, width):

    # reading data
    workbook1 = xlrd.open_workbook("Equity_Distribution_Data.xlsx")
    worksheet1 = workbook1.sheet_by_index(0)

    def gen_equities(wksht):
        keep_going = True
        index = 1

        while keep_going:
            try:
                equity_cell = wksht.cell(index, 1)
                equity = equity_cell.value
                index += 1
                yield equity

            except IndexError:
                keep_going = False

    equities = list(gen_equities(worksheet1))

    # creating new distribution data
    def gen_dist(dst_st, wdh):
        incrament = round(100.0 / dst_st, 2)

        for index in range(dst_st):
            coord = index * incrament
            count = 0

            for equity in equities:
                if (-wdh) < (equity - coord) <= wdh:
                    count += 1

            yield coord, count

    data_set = list(gen_dist(distinct_sets, width))

    # writing new data to sheet
    workbook2 = xlwt.Workbook("Equity_Distribution_Data_MOD.xlsx")
    worksheet2 = workbook2.add_worksheet()

    worksheet2.write(0, 0, "Equity")
    worksheet2.write(0, 1, "Density")

    row = 1

    for item in data_set:
        worksheet2.write(row, 0, item[0])
        worksheet2.write(row, 1, item[1])

        row += 1

    workbook2.close()
