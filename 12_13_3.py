import xlwt
import xlrd
from xlutils.copy import copy
workbook = xlrd.open_workbook('exmaple00.xls')
sheet1 = workbook.sheet_by_index(0)

new_book = copy(workbook)
sheet2 = new_book.get_sheet(0)


for x in range(0,sheet1.ncols):
    for d in range(0,sheet1.nrows):
        values = sheet1.cell(d,x).value
        sheet2.write(x,d,values)
        sheet2.write(20,d,' ')
        sheet2.write(21,d,' ')
        sheet2.write(22,d,' ')
new_book.save('exmaple001.xls')
