from matplotlib import pyplot
from openpyxl import load_workbook


def extract_value(cell):
    return cell.value


wb = load_workbook('data_analysis_lab.xlsx')

a_column = list(map(extract_value, wb['Data']['A'][1:]))
b_column = list(map(extract_value, wb['Data']['B'][1:]))
c_column = list(map(extract_value, wb['Data']['C'][1:]))
d_column = list(map(extract_value, wb['Data']['D'][1:]))

pyplot.plot(a_column, c_column, label='График 1')
pyplot.plot(a_column, d_column, label='График 2')

pyplot.xlabel('Относительная температура')
pyplot.ylabel('Год')
pyplot.legend(loc='upper right')
pyplot.show()