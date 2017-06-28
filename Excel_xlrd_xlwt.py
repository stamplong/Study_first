import xlrd
import xlwt
from datetime import date,datetime

workbook = xlrd.open_workbook(r'example.xlsx')
print workbook.sheet_names()
sheet1 = workbook.sheet_names()[0]
print sheet1
print "*"*20
print workbook.nsheets
sheet2 = workbook.sheet_by_index(0)
print sheet2.name
print sheet2.nrows
print sheet2.ncols

print sheet2.row_values(3)
print sheet2.col_values(1)
print "*"*10

print sheet2.cell(0,0).value
print sheet2.cell_value(0,0)
print sheet2.row(0)[0].value
date = sheet2.cell(18,1).ctype
print date
print "***---"*15
print sheet2.name

from datetime import datetime
style0 = xlwt.easyxf('font:name Time new roman,color-index orange,bold on',num_format_str='#,###.##')
style1 = xlwt.easyxf(num_format_str='%Y/%m/%d')

wb = xlwt.Workbook()
ws = wb.add_sheet('new test sheet')

ws.write(0,0,1234.56,style0)
ws.write(1,0,datetime.now(),style1)
ws.write(2,0,1)
ws.write(2,1,1)
ws.write(2,2,xlwt.Formula("A3+B3"))
wb.save('example1.xls')
